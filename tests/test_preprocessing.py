import pandas as pd
import numpy as np
from src.preprocessing.data_cleaner import limpar_e_dividir_dados

def test_tratamento_valores_ausentes():
    """
    Testa se o pré-processamento limpa corretamente os valores nulos injetados.
    """
    # Aumentamos para 10 registros para que o split de 20% (2 linhas) comporte as duas classes na estratificação
    dados_mock = {
        'id_cliente': [f'TELCO-{i}' for i in range(10)],
        'idade': [25, 40, 31, 65, 22, 35, 48, 54, 29, 61],
        'meses_contrato': [10, 2, 24, 36, 1, 12, 6, 48, 15, 70],
        'tipo_contrato': ['Anual', 'Mensal', 'Bienal', 'Anual', 'Mensal', 'Mensal', 'Anual', 'Bienal', 'Mensal', 'Bienal'],
        'cobranca_mensal': [50.0, 80.0, 45.0, 110.0, 30.0, 70.0, 55.0, 95.0, 65.0, 115.0],
        'total_gasto': [500.0, np.nan, 1080.0, 3960.0, 30.0, 840.0, np.nan, 4560.0, 975.0, 8050.0], # Injeta nulos para testar a limpeza
        'churn': [0, 1, 0, 0, 1, 0, 0, 1, 0, 0]
    }
    df_teste_unitario = pd.DataFrame(dados_mock)
    
    # Executa a lógica de limpeza do projeto
    df_tr, df_te = limpar_e_dividir_dados(df_teste_unitario)
    df_unificado = pd.concat([df_tr, df_te])
    
    # Asserções e validações do teste unitário
    assert df_unificado['total_gasto'].isnull().sum() == 0, "O pipeline falhou: ainda existem valores nulos no total_gasto."
    assert 'id_cliente' not in df_unificado.columns, "O pipeline falhou: a coluna id_cliente não foi descartada."