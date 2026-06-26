from src.ingestion.ingest import simular_ou_carregar_dados
from src.preprocessing.data_cleaner import limpar_e_dividir_dados
from src.features.feature_engineering import extrair_e_normalizar_features
from src.models.train import treinar_modelo_classificacao
from src.evaluation.evaluate import avaliar_e_salvar_metricas

def pipeline_principal():
    print("--- INICIANDO PIPELINE INCREMENTAL ---")
    
    # Definição dos caminhos locais de arquivos
    caminho_dados_brutos = "data/raw/dados_telecom.csv"
    caminho_modelo_salvo = "models_saved/modelo_churn_rf.pkl"
    caminho_metricas = "metrics/metricas_finais.json"
    
    # Etapa 1: Ingestão/Coleta de Dados
    df_bruto = simular_ou_carregar_dados(caminho_dados_brutos)
    
    # Etapa 2: Pré-processamento e Limpeza (Remoção de Nulos e Split)
    df_treino, df_teste = limpar_e_dividir_dados(df_bruto)
    
    # Etapa 3: Engenharia de Atributos e Escalonamento
    X_train, X_test, y_train, y_test = extrair_e_normalizar_features(df_treino, df_teste)
    
    # Etapa 4: Treinamento e Persistência do Algoritmo
    modelo = treinar_modelo_classificacao(X_train, y_train, caminho_modelo_salvo)
    
    # Etapa 5: Validação e Avaliação Final
    avaliar_and_salvar = avaliar_e_salvar_metricas(modelo, X_test, y_test, caminho_metricas)
    
    print("--- PIPELINE CONCLUÍDO COM SUCESSO ---")

if __name__ == "__main__":
    pipeline_principal()