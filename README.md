# Receita Federal Web Scraping com AWS e Airflow

Este repositório contém um projeto de web scraping para extrair, processar e atualizar dados da Receita Federal do Brasil. Utiliza AWS para armazenamento e processamento, Airflow para gerenciamento de workflows e a API do Google para buscas, respeitando os limites de uso.

## Funcionalidades

- Coleta de dados públicos da Receita Federal
- Processamento e limpeza dos dados coletados
- Atualização de dados para evitar duplicações
- Armazenamento dos dados na AWS
- Gerenciamento de workflows com Apache Airflow
- Utilização da API do Google para buscas automatizadas

## Estrutura do Projeto

- `dags/`: Definições de workflows do Airflow
- `scripts/`: Scripts de scraping e processamento de dados
- `requirements.txt`: Dependências do projeto
- `config/`: Arquivos de configuração para AWS, Airflow e API do Google

## Requisitos

- Python 3.x
- AWS CLI configurado
- Apache Airflow
- Credenciais para a API do Google

### Principais Bibliotecas

- BeautifulSoup
- Requests
- Pandas
- Boto3 (para interação com AWS)
- Google API Client
