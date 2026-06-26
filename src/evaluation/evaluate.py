import os
import json
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

def avaliar_e_salvar_metricas(model, X_test, y_test, json_path: str):
    """
    Mede a performance do modelo usando as métricas obrigatórias do item 4.8.
    
    :param model: Modelo carregado ou treinado.
    :param X_test: Features de teste.
    :param y_test: Labels reais de teste.
    :param json_path: Onde salvar o arquivo de texto com as métricas.
    """
    print("[AVALIAÇÃO] Gerando previsões e calculando indicadores...")
    y_pred = model.predict(X_test)
    
    # Coleta das métricas exigidas
    metricas = {
        "Acurácia": round(float(accuracy_score(y_test, y_pred)), 4),
        "Precisão": round(float(precision_score(y_test, y_pred)), 4),
        "Recall": round(float(recall_score(y_test, y_pred)), 4),
        "F1-Score": round(float(f1_score(y_test, y_pred)), 4)
    }
    
    # Print elegante no terminal para a apresentação
    print("\n" + "="*30)
    print("      MÉTRICAS DE AVALIAÇÃO   ")
    print("="*30)
    for metrica, valor in metricas.items():
        print(f" -> {metrica}: {valor * 100:.2f}%")
    print("="*30)
    
    print("\nMatriz de Confusão:")
    print(confusion_matrix(y_test, y_pred))
    print("="*30 + "\n")
    
    # Salvando os resultados em JSON
    os.makedirs(os.path.dirname(json_path), exist_ok=True)
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(metricas, f, indent=4, ensure_ascii=False)
    print(f"[AVALIAÇÃO] Arquivo de métricas exportado para: {json_path}")