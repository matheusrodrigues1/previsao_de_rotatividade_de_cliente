# Projeto de Inteligência Computacional: Predição de Churn em Telecomunicações

## 1. Explicação do Problema (Contexto de Negócio)
A rotatividade de clientes (*Churn*) é um dos maiores gargalos financeiros de empresas prestadoras de serviços de Telecomunicação. Reter um cliente antigo custa cerca de 5 vezes menos do que adquirir um cliente novo através de campanhas de publicidade. 

Este projeto constrói um pipeline de Inteligência Computacional baseado no algoritmo **Random Forest Classifier** para prever se um determinado consumidor cancelará ou não o serviço contratado.

## 2. Estrutura do Dataset Utilizado
O projeto consome uma base de dados simulando cenários reais de mercado (como o dataset *Telco Customer Churn* do Kaggle), contendo as seguintes variáveis:
* `idade`: Inteiro representando a idade do usuário.
* `meses_contrato`: Tempo de permanência do cliente na base da empresa.
* `tipo_contrato`: Tipo de faturamento (`Mensal`, `Anual`, `Bienal`).
* `cobranca_mensal`: Custo financeiro regular do plano do cliente.
* `total_gasto`: Valor bruto acumulado investido pelo cliente.
* `gasto_proporcional_tempo` (*Nova Feature*): Razão do total gasto dividido pelos meses ativos.
* `churn` (*Target*): Variável binária onde `1` significa que o cliente cancelou e `0` que continuou ativo.

## 🚀 3. Instruções de Execução

Certifique-se de estar com o ambiente virtual criado e ativo no terminal antes de prosseguir.

### Passo 1: Instalação das bibliotecas e dependências
```bash
pip install -r requirements.txt
```
### Passo 2: Executar a suíte de Testes Unitários (Garantia de Qualidade)
```bash
pytest tests/
```
### Passo 3: Executar o pipeline completo
```bash
python main.py
```

## 4. Bibliotecas Utilizadas
- pandas e numpy: Engenharia de features, manipulação matricial e higienização das tabelas.

- scikit-learn: Implementação do Hold-out, Padronização dos dados e treinamento do classificador Random Forest.

- joblib: Armazenamento binário serializado do modelo treinado na pasta models_saved/.

- pytest: Automatização de testes unitários de entrada.
