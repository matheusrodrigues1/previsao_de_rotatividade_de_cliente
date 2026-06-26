import os
import pandas as pd
from sklearn.model_selection import train_test_split

def limpar_e_dividir_dados(df: pd.DataFrame) -> tuple:
    """
    Executa a limpeza dos dados (valores ausentes e remoção de IDs),
    salva a base limpa na pasta 'processed' e separa em treino/teste.
    Conforme item 4.4 e 4.7 do edital.
    
    :param df: DataFrame bruto vindo da ingestão.
    :return: Tupla com (df_train, df_test)
    """
    print("[PRÉ-PROCESSAMENTO] Iniciando limpeza e tratamento de dados...")
    df_clean = df.copy()
    
    # Remoção de identificadores textuais irrelevantes para o modelo
    if 'id_cliente' in df_clean.columns:
        df_clean = df_clean.drop(columns=['id_cliente'])
        
    # Tratamento de valores ausentes (Imputação pela mediana)
    if df_clean['total_gasto'].isnull().sum() > 0:
        mediana_gasto = df_clean['total_gasto'].median()
        df_clean['total_gasto'] = df_clean['total_gasto'].fillna(mediana_gasto)
        print(f"[PRÉ-PROCESSAMENTO] Valores nulos em 'total_gasto' preenchidos com a mediana ({mediana_gasto:.2f}).")
    
    # --- NOVO: Salvando o arquivo limpo na pasta data/processed/ ---
    caminho_processado = "data/processed/dados_limpos.csv"
    os.makedirs(os.path.dirname(caminho_processado), exist_ok=True)
    df_clean.to_csv(caminho_processado, index=False)
    print(f"[PRÉ-PROCESSAMENTO] Dados limpos e unificados salvos em: {caminho_processado}")
    # ---------------------------------------------------------------
        
    # Divisão treino (80%) e teste (20%) mantendo a proporção do Churn (stratify)
    df_train, df_test = train_test_split(
        df_clean, 
        test_size=0.2, 
        random_state=42, 
        stratify=df_clean['churn']
    )
    
    return df_train, df_test