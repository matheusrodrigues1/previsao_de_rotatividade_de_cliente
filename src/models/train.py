import os
import joblib
from sklearn.ensemble import RandomForestClassifier

def treinar_modelo_classificacao(X_train, y_train, output_path: str) -> RandomForestClassifier:
    """
    Treina o algoritmo Random Forest conforme item 4.6 e persiste em disco conforme item 7.
    Aplica pesos balanceados para corrigir o problema de Recall zerado.
    
    :param X_train: Features de treino escalonadas.
    :param y_train: Labels de treino.
    :param output_path: Onde o arquivo .pkl do modelo será salvo.
    :return: Modelo treinado.
    """
    print("[MODELAGEM] Treinando classificador Random Forest (Inteligência Computacional)...")
    
    # ADICIONADO: class_weight="balanced" força o modelo a prestar atenção no Churn
    modelo = RandomForestClassifier(
        n_estimators=150, 
        max_depth=5, 
        class_weight="balanced", 
        random_state=42
    )
    modelo.fit(X_train, y_train)
    
    # Salvando o artefato do modelo
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    joblib.dump(modelo, output_path)
    print(f"[MODELAGEM] Modelo persistido com sucesso em: {output_path}")
    
    return modelo