import pandas as pd
from sklearn.preprocessing import StandardScaler

def aplicar_mapeamento_manual(df: pd.DataFrame) -> pd.DataFrame:
    """
    Codifica variáveis categóricas ordinais em números estruturados.
    """
    df_res = df.copy()
    mapa_contrato = {'Mensal': 0, 'Anual': 1, 'Bienal': 2}
    df_res['tipo_contrato'] = df_res['tipo_contrato'].map(mapa_contrato)
    return df_res

def extrair_e_normalizar_features(df_train: pd.DataFrame, df_test: pd.DataFrame) -> tuple:
    """
    Aplica codificação, cria novas features e normaliza os dados de forma isolada.
    Conforme item 4.5 (Criação de Features) e 4.4 (Normalização).
    
    :param df_train: Dataset de treino limpo.
    :param df_test: Dataset de teste limpo.
    :return: Matrizes prontas X_train, X_test e os alvos y_train, y_test
    """
    print("[ENGENHARIA DE FEATURES] Codificando variáveis e gerando novos atributos...")
    
    # Codificação categórica
    df_tr = aplicar_mapeamento_manual(df_train)
    df_te = aplicar_mapeamento_manual(df_test)
    
    # Criação de Nova Feature: Razão de cobrança por tempo de contrato (Fidelidade Financeira)
    # Evita divisão por zero somando 1 aos meses
    df_tr['gasto_proporcional_tempo'] = df_tr['total_gasto'] / (df_tr['meses_contrato'] + 1)
    df_te['gasto_proporcional_tempo'] = df_te['total_gasto'] / (df_te['meses_contrato'] + 1)
    
    # Divisão de variáveis preditivas (X) e alvo (y)
    X_train = df_tr.drop(columns=['churn'])
    y_train = df_tr['churn']
    X_test = df_te.drop(columns=['churn'])
    y_test = df_te['churn']
    
    # Padronização (Z-score) das colunas numéricas
    colunas_numericas = ['idade', 'meses_contrato', 'cobranca_mensal', 'total_gasto', 'gasto_proporcional_tempo']
    scaler = StandardScaler()
    
    X_train[colunas_numericas] = scaler.fit_transform(X_train[colunas_numericas])
    X_test[colunas_numericas] = scaler.transform(X_test[colunas_numericas]) # Apenas transform no teste
    
    return X_train, X_test, y_train, y_test