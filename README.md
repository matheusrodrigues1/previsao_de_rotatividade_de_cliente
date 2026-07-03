# Projeto de Inteligência Computacional: Predição de Churn em Telecomunicações

## 📌 Contexto de Negócio

A rotatividade de clientes (*Churn*) é um dos maiores desafios financeiros das empresas de telecomunicações. Reter clientes existentes costuma ser significativamente mais barato do que conquistar novos clientes.

Este projeto utiliza técnicas de Inteligência Computacional e Machine Learning, implementando o algoritmo **Random Forest Classifier** para prever se um cliente possui probabilidade de cancelar o serviço.

---

## 📂 Estrutura do Projeto

```text
PROJETO_ML/
│
├── .pytest_cache/            # Cache gerado pelo pytest
├── data/
│   ├── processed/            # Dados tratados e prontos para treinamento
│   └── raw/                  # Dados brutos originais
├── metrics/                  # Métricas e relatórios gerados pelo modelo
├── models_saved/             # Modelos treinados salvos em disco
├── src/
│   ├── evaluation/           # Avaliação do desempenho do modelo
│   ├── features/             # Engenharia de atributos (Feature Engineering)
│   ├── ingestion/            # Leitura e carregamento dos dados
│   ├── models/               # Treinamento e utilização dos modelos
│   ├── preprocessing/        # Limpeza e pré-processamento dos dados
│   └── __init__.py
├── tests/                    # Testes automatizados
└── venv/                     # Ambiente virtual do projeto
```

---

# 🚀 Como Executar o Projeto

## 1. Clonar o repositório

```bash
git clone [(https://github.com/matheusrodrigues1/previsao_de_rotatividade_de_cliente/tree/main)]
cd PROJETO_ML
```

---

## 2. Criar o ambiente virtual

### Windows

```bash
python -m venv venv
```

### Linux/macOS

```bash
python3 -m venv venv
```

---

## 3. Ativar o ambiente virtual

### Windows (CMD)

```bash
venv\Scripts\activate
```

### Windows (PowerShell)

```powershell
.\venv\Scripts\Activate.ps1
```

Caso ocorra erro de permissão:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Depois execute novamente:

```powershell
.\venv\Scripts\Activate.ps1
```

### Linux/macOS

```bash
source venv/bin/activate
```

---

## Verificando se o ambiente está ativo

Se o ambiente virtual estiver ativo, o terminal ficará semelhante a:

```bash
(venv) C:\PROJETO_ML>
```

ou

```bash
(venv) usuario@pc:~/PROJETO_ML$
```

---

## 4. Instalar as dependências

```bash
pip install -r requirements.txt
```

---

## 5. Executar os testes automatizados

```bash
pytest tests/
```

---

## 6. Executar o projeto

```bash
python main.py
```

---

## Fluxo de execução

O pipeline executa as seguintes etapas:

1. Leitura dos dados brutos (`data/raw`);
2. Pré-processamento dos dados;
3. Engenharia de atributos;
4. Separação entre treino e teste;
5. Treinamento do modelo Random Forest;
6. Avaliação do desempenho;
7. Salvamento do modelo em `models_saved`;
8. Geração das métricas em `metrics`.

---

## Desativar o ambiente virtual

Ao finalizar:

```bash
deactivate
```

---

# 📚 Bibliotecas Utilizadas

- **pandas** e **numpy**: manipulação e tratamento dos dados;
- **scikit-learn**: pré-processamento, treinamento e avaliação do modelo;
- **joblib**: serialização e salvamento do modelo treinado;
- **pytest**: execução dos testes automatizados.

---
