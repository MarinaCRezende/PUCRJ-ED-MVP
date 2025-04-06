# PUCRJ-ED-MVP
Projeto MVP para compor nota da Pós Graduação de Ciência de Dados e Analytics, Sprint de Engenharia de Dados, na PUC-RJ
Link para acesso ao código publicado no Databricks Community: https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/2263258057188516/2676582161827454/799048061560195/latest.html

# 📊 Pipeline de Dados Portuários com Spark em Databricks

Este projeto é parte do MVP da Sprint de Engenharia de Dados do curso de Pós-Graduação em Ciência de Dados e Analytics. O objetivo é criar um pipeline de ingestão, tratamento e análise de dados estatísticos aquaviários do Brasil, utilizando tecnologias na nuvem com foco no Databricks e Apache Spark.

## 🚢 Contexto

O setor portuário brasileiro é essencial para a movimentação de cargas. Uma análise adequada desses dados pode:
- Melhorar a gestão de portos,
- Reduzir custos operacionais,
- Otimizar processos de atracação, carregamento e transporte.

## 🎯 Objetivo

Responder, de forma rápida e clara, a perguntas estratégicas usando dados históricos disponibilizados pela ANTAQ:

1. Qual é o tempo médio de atracação por porto?
2. Qual o volume total de carga movimentada por ano?
3. Qual é o total movimentado por tipo de carga?
4. Quais são os terminais portuários mais utilizados?
5. Quais são os portos com maior número de atracações?
6. Quais tipos de mercadoria são mais movimentados por navegação de longo curso?
7. Qual o tempo médio de viagem por tipo de navio?

## 📁 Fonte de Dados

**Estatístico Aquaviário - ANTAQ**  
🔗 [Acesse aqui](https://web3.antaq.gov.br/ea/sense/download.html#pt)  
Período coberto: **2020 a 2024**

### Tabelas utilizadas:
- Atracação
- Carga
- Carga Conteinerizada
- Tempos de Atracação
- Taxa de Ocupação
- Carga por Região Hidrográfica, Hidrovia e Rio

## 🛠️ Tecnologias

- **Apache Spark (PySpark)**
- **SQL**
- **Databricks**
- **Python**
- **DBFS (Databricks File System)**
- **Pandas (para manipulação auxiliar de dados)**

## 🔄 Pipeline

1. **Leitura dos arquivos CSV armazenados no DBFS**
2. **Tratamento de arquivos particionados (.txt_part)**
3. **União dos dados de diferentes partes**
4. **Padronização dos nomes das colunas**
5. **Visualização dos dados via SQL**

## 🧪 Execução no Databricks

- O código deve ser executado em um notebook no ambiente Databricks.
- Os arquivos .txt devem estar previamente carregados na pasta `/FileStore/tables/` do DBFS.
- Algumas operações requerem permissões de escrita/leitura no cluster em uso.
- A leitura dos arquivos assume o uso de delimitador `;` e presença de cabeçalho.

## 🌐 Acesso ao Projeto

Você pode acessar o notebook completo neste link:  
🔗 [Databricks Notebook](https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/2263258057188516/2676582161827454/799048061560195/latest.html)

## 📌 Observações

- Os dados particionados são reunidos automaticamente com base em padrões de nomenclatura dos arquivos.
- Nomes de colunas são limpos para evitar problemas com caracteres especiais.

## 👩🏻‍💻 Autora

**Marina Rezende**  
Projeto desenvolvido como parte da formação em Engenharia de Dados.
"""

