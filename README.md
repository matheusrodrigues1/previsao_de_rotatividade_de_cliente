# Projeto de Inteligência Computacional: Predição de Churn em Telecomunicações

## 📌 1. Explicação do Problema (Contexto de Negócio)

A rotatividade de clientes (*Churn*) é um dos maiores gargalos financeiros de empresas prestadoras de serviços de Telecomunicação. Reter um cliente antigo custa cerca de **5 vezes menos** do que adquirir um cliente novo por meio de campanhas de marketing e publicidade.

Este projeto implementa um pipeline de Inteligência Computacional utilizando o algoritmo **Random Forest Classifier** para prever se um cliente cancelará ou não o serviço contratado.

---

## 📊 2. Estrutura do Dataset Utilizado

O projeto utiliza uma base de dados que simula cenários reais de mercado, inspirada no dataset **Telco Customer Churn**, contendo as seguintes variáveis:

| Variável | Descrição |
|----------|------------|
| `idade` | Idade do cliente |
| `meses_contrato` | Tempo de permanência do cliente na empresa |
| `tipo_contrato` | Tipo de faturamento (`Mensal`, `Anual`, `Bienal`) |
| `cobranca_mensal` | Valor mensal pago pelo cliente |
| `total_gasto` | Valor total gasto pelo cliente |
| `gasto_proporcional_tempo` | Total gasto dividido pelos meses ativos |
| `churn` | Variável alvo: `1` = cancelou o serviço, `0` = permaneceu ativo |

---

# 📁 Estrutura do Projeto

```text
projeto-churn/
│
├── data/
├── models_saved/
├── tests/
├── main.py
├── requirements.txt
├── README.md
└── venv/
```

---

# 🚀 3. Como Executar o Projeto

## Pré-requisitos

- Python 3.10 ou superior instalado;
- Git (opcional);
- Terminal ou Prompt de Comando.

Verifique a instalação do Python:

```bash
python --version
```

ou

```bash
python3 --version
```

---

## Passo 1: Clonar o projeto (opcional)

```bash
git clone <url-do-repositorio>
cd projeto-churn
```

---

## Passo 2: Criar o Ambiente Virtual (venv)

### Windows

```bash
python -m venv venv
```

### Linux/macOS

```bash
python3 -m venv venv
```

Após esse comando, será criada uma pasta chamada:

```text
venv/
```

que conterá todas as dependências isoladas do projeto.

---

## Passo 3: Ativar o Ambiente Virtual

### Windows (Prompt de Comando - CMD)

```bash
venv\Scripts\activate
```

### Windows (PowerShell)

```bash
.\venv\Scripts\Activate.ps1
```

Caso apareça um erro de permissão no PowerShell, execute:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Depois:

```powershell
.\venv\Scripts\Activate.ps1
```

### Linux/macOS

```bash
source venv/bin/activate
```

---

## Como saber se o ambiente virtual está ativo?

Após ativar, o terminal ficará semelhante a:

```bash
(venv) C:\projeto-churn>
```

ou

```bash
(venv) usuario@pc:~/projeto-churn$
```

O prefixo `(venv)` indica que o ambiente virtual está ativo.

---

## Passo 4: Instalar as Dependências

Com o ambiente virtual ativo, execute:

```bash
pip install -r requirements.txt
```

---

## Passo 5: Executar os Testes Unitários

Para validar o funcionamento das principais funcionalidades:

```bash
pytest tests/
```

---

## Passo 6: Executar o Pipeline Completo

```bash
python main.py
```

O sistema realizará:

1. Carregamento dos dados;
2. Engenharia de atributos (*Feature Engineering*);
3. Pré-processamento dos dados;
4. Separação em treino e teste;
5. Treinamento do modelo Random Forest;
6. Avaliação de desempenho;
7. Salvamento do modelo treinado na pasta `models_saved/`.

---

## Passo 7: Desativar o Ambiente Virtual

Ao terminar o uso do projeto:

```bash
deactivate
```

---

# 📚 4. Bibliotecas Utilizadas

### Pandas e NumPy
- Manipulação de dados;
- Limpeza e transformação de tabelas;
- Operações matemáticas e matriciais.

### Scikit-Learn
- Pré-processamento dos dados;
- Divisão de treino e teste (*Hold-out*);
- Implementação do algoritmo Random Forest Classifier;
- Métricas de avaliação.

### Joblib
- Serialização e armazenamento do modelo treinado na pasta `models_saved/`.

### Pytest
- Automatização dos testes unitários do projeto.

---

# 🎯 Objetivo do Projeto

Desenvolver um modelo de Inteligência Computacional capaz de identificar clientes com maior probabilidade de cancelamento do serviço, permitindo que empresas de telecomunicações adotem estratégias de retenção de forma proativa e baseada em dados.
