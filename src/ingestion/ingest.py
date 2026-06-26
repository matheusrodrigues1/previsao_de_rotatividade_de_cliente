import os
import pandas as pd
import numpy as np

def simular_ou_carregar_dados(filepath: str) -> pd.DataFrame:
    """
    Carrega o dataset de Telecom ou gera dados sintéticos caso o arquivo não exista.
    Conforme item 4.2: Define fonte, registros, variáveis e tipos.
    
    :param filepath: Caminho do arquivo CSV de entrada.
    :return: DataFrame com os dados brutos.
    """
    if os.path.exists(filepath):
        print(f"[INGESTÃO] Carregando dados existentes de: {filepath}")
        return pd.read_csv(filepath)
    
    print("[INGESTÃO] Arquivo não encontrado. Gerando dados simulados (Telco Churn Dataset)...")
    np.random.seed(42)
    n_registros = 1200
    
    dados = {
        'id_cliente': [f"TELCO-{i:04d}" for i in range(n_registros)],
        'idade': np.random.randint(18, 85, size=n_registros),
        'meses_contrato': np.random.randint(1, 74, size=n_registros),
        'tipo_contrato': np.random.choice(['Mensal', 'Anual', 'Bienal'], size=n_registros, p=[0.5, 0.3, 0.2]),
        'cobranca_mensal': np.round(np.random.uniform(25.0, 130.0, size=n_registros), 2),
        'total_gasto': np.nan, # Será preenchido abaixo com alguns valores nulos propositais
        'churn': np.random.choice([0, 1], size=n_registros, p=[0.78, 0.22])
    }
    
    df = pd.DataFrame(dados)
    df['total_gasto'] = df['meses_contrato'] * df['cobranca_mensal']
    
    # Injeta 40 valores nulos (ausentes) para forçar o tratamento no pré-processamento
    df.loc[df.sample(n=40, random_state=42).index, 'total_gasto'] = np.nan
    
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    df.to_csv(filepath, index=False)
    print(f"[INGESTÃO] Dataset criado com {n_registros} registros em: {filepath}")
    return df