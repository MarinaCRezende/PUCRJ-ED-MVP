# Databricks notebook source
# MAGIC %md # Pipeline de dados utilizando tecnologias na nuvem: Estudo dos dados estatísticos aquaviários do Brasil
# MAGIC
# MAGIC
# MAGIC #### MVP referente à sprint de Engenharia de Dados
# MAGIC #### Curso de Pós Graduação em Ciência de Dados e Analytics
# MAGIC
# MAGIC
# MAGIC ## Introdução
# MAGIC
# MAGIC O setor portuário possui um papel de destaque, por movimentar grande parte da carga no país. Saber o que acontece dentro e fora de um porto, na relação do porto com a malha viária externa, identificar percurso de cargas, tempo de estadia, padrão de estadual de navios, tudo isso pode ser extraído com diversas combinações de dados se bem organizados e consultados de forma estratégica. Neste contexto, a análise de dados portuários pode fornecer informações valiosas que podem melhorar a gestão de portos, reduzir custos operacionais e conduzir operações de carregamento/pesagem para um desempenho melhor.
# MAGIC
# MAGIC
# MAGIC ## Objetivo
# MAGIC
# MAGIC O principal objetivo deste trabalho é desenvolver um pipeline de dados utilizando tecnologias na nuvem. Os dados escolhidos foram de dados portuários brasileiros, permitindo responder, de forma clara e rápida, perguntas relevantes para a gestão e planejamento das operações portuárias. A partir das tabelas de dados escolhida, o objetivo será responder às seguints questões: 
# MAGIC
# MAGIC 1. Qual é o tempo médio de atracação por porto?
# MAGIC
# MAGIC 2. Qual o volume total de carga movimentada por ano?
# MAGIC
# MAGIC 3. Qual é o total movimentado por tipo de carga?
# MAGIC
# MAGIC 4. Quais são os terminais portuários mais utilizados?
# MAGIC
# MAGIC 5. Quais são os portos com maior número de atracações?
# MAGIC
# MAGIC 6. Quais tipos de mercadoria são mais movimentados por navegação de longo curso?
# MAGIC
# MAGIC 7. Qual o tempo médio de viagem por tipo de navio?
# MAGIC
# MAGIC
# MAGIC
# MAGIC ## Decrição de Dados
# MAGIC #### Fonte:
# MAGIC Estatístico Aquaviário - ANTAQ
# MAGIC https://web3.antaq.gov.br/ea/sense/download.html#pt
# MAGIC
# MAGIC #### Dados de:
# MAGIC 1. Atracação
# MAGIC 2. Carga
# MAGIC 3. Carga Conteinerizada
# MAGIC 4. Tempos Atracação
# MAGIC 5. Taxa Ocupação
# MAGIC 6. Carga Região Hidrográfica, Hidrovia e Rio
# MAGIC
# MAGIC #### Período: Anos de 2020 a 2024.
# MAGIC
# MAGIC "O Sistema de Desempenho Portuário – SDP é a principal fonte de dados para disponibilização das estatísticas apresentadas no Estatístico Aquaviário. Os dados presentes no SDP são declarados pelas Autoridades Portuárias (portos organizados) e pelos Terminais Autorizados pela Antaq, sendo estes dados recebidos diariamente via arquivos ou por preenchimento em formulário do próprio sistema SDP. Há, também, a agregação de dados da hidrovia Paraná-Tietê enviados mensalmente em planilha pela Administração da Hidrovia do Paraná – Ahrana." - ANTAQ <https://web3.antaq.gov.br/ea/sense/doc.html#pt>
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ## Preparação dos dados

# COMMAND ----------

# MAGIC %md
# MAGIC Importar das Bibliotecas

# COMMAND ----------

import pandas as pd
import glob
import os
import re

from pyspark.sql import DataFrame
from pyspark.sql import SparkSession
from collections import defaultdict
from pyspark.sql import functions as F
from pyspark.sql.functions import col, coalesce, lit  


# COMMAND ----------

# MAGIC %md
# MAGIC Confirmar o upload correto dos arquivos:

# COMMAND ----------

dbutils.fs.ls("dbfs:/FileStore/tables/")

# COMMAND ----------

# MAGIC %md
# MAGIC Excluindo arquivo desnecessário:

# COMMAND ----------

dbutils.fs.rm("dbfs:/FileStore/tables/2020Carga_part1.txt", True)


# COMMAND ----------

# MAGIC %md
# MAGIC Criando um Dataframe com todas as tabelas:

# COMMAND ----------


# Criando sessão Spark (caso ainda não tenha sido criada)
spark = SparkSession.builder.appName("CargaDados").getOrCreate()

# Caminho base no DBFS
caminho_dbfs = "dbfs:/FileStore/tables/"

# Listar os arquivos dentro do diretório
arquivos_dbfs = dbutils.fs.ls(caminho_dbfs)

# Criar um dicionário para armazenar os DataFrames individuais
dfs_individuais = {}

# Importar cada arquivo separadamente
for arquivo in arquivos_dbfs:
    caminho_arquivo = arquivo.path
    
    if caminho_arquivo.endswith(".txt") or "txt_part" in caminho_arquivo:
        nome_tabela = caminho_arquivo.split("/")[-1].replace(".txt", "").replace(".txt_part1", "").replace(".txt_part2", "").replace(".txt_part3", "")
        
        df = spark.read.option("header", "true").option("sep", ";").csv(caminho_arquivo)
        
        dfs_individuais[nome_tabela] = df  # Salvar DataFrame no dicionário
        
        print(f"Arquivo importado: {nome_tabela}")

# Conferindo quantos arquivos foram carregados
print(f"Total de arquivos carregados: {len(dfs_individuais)}")



# COMMAND ----------

# MAGIC %md
# MAGIC Unindo as tabelas particionadas:

# COMMAND ----------



# Criar um dicionário para armazenar listas de DataFrames de tabelas particionadas
particoes_dict = defaultdict(list)
dfs_consolidados = {}  # Dicionário final consolidado

# Separar os arquivos que possuem múltiplas partes
for nome_tabela, df in dfs_individuais.items():
    if "_txt_part" in nome_tabela:  
        base_tabela = nome_tabela.split("_txt_part")[0]  # Obtém o nome base (ex.: "2020Carga")
        particoes_dict[base_tabela].append(df)  # Agrupa todas as partes
    else:
        dfs_consolidados[nome_tabela] = df  # Mantém tabelas já completas

# Unir as partes de cada tabela e armazenar no dicionário final
for base_tabela, lista_dfs in particoes_dict.items():
    if lista_dfs:  
        df_unificado = lista_dfs[0]  # Começa com o primeiro DataFrame
        for df_part in lista_dfs[1:]:  # União das partes restantes
            df_unificado = df_unificado.union(df_part)

        dfs_consolidados[base_tabela] = df_unificado  # Substitui as versões particionadas

print(f"Tabelas consolidadas corretamente: {list(dfs_consolidados.keys())}")



# COMMAND ----------

# MAGIC %md
# MAGIC Confirmando a união das tabelas

# COMMAND ----------

df.columns


# COMMAND ----------


def clean_column_names(df):
    # Mapeamento de caracteres para substituição
    replace_map = {
        " ": "_", ";": "", "{": "", "}": "", "(": "", ")": "",
        "\n": "", "\t": "", "=": "", "º":"o",
        "é": "e", "á": "a", "ã": "a", "ç": "c", "í": "i", "ó": "o",
        "ú": "u", "â": "a", "ê": "e", "ô": "o", "à": "a", "è": "e",
        "ì": "i", "ò": "o", "ù": "u", "ü": "u", "ï": "i", "ö": "o",
        "ñ": "n", "õ": "o", "ý": "y", "ÿ": "y",
        "Á": "a", "É": "e", "Í": "i", "Ó": "o", "Ú": "u", "Â": "a",
        "Ê": "e", "Ô": "o", "À": "a", "È": "e", "Ì": "i", "Ò": "o",
        "Ù": "u", "Ü": "u", "Ï": "i", "Ö": "o", "Ñ": "n", "Õ": "o",
        "Ý": "y", "Ÿ": "y"
    }

    cleaned_columns = []
    for col in df.columns:
        new_col = col
        # Substitui caracteres conforme o dicionário
        for old_char, new_char in replace_map.items():
            new_col = new_col.replace(old_char, new_char)
        # Converte para minúsculas
        new_col = new_col.lower()
        # Substitui caracteres especiais e prefixos com números
        new_col = re.sub(r'\W|^(?=\d)', '_', new_col)
        cleaned_columns.append(new_col)

    # Renomeando as colunas no DataFrame
    for old_name, new_name in zip(df.columns, cleaned_columns):
        df = df.withColumnRenamed(old_name, new_name)

    return df

# Aplicando a função de limpeza a todos os DataFrames no dicionário dfs_consolidados
for nome_tabela, df in dfs_consolidados.items():
    dfs_consolidados[nome_tabela] = clean_column_names(df)

# Verifique os novos nomes das colunas de um DataFrame de exemplo
print(dfs_consolidados[list(dfs_consolidados.keys())[0]].columns)



# COMMAND ----------

# MAGIC %md
# MAGIC Criação do esquema bronze

# COMMAND ----------

spark.sql("CREATE SCHEMA IF NOT EXISTS bronze")

# COMMAND ----------

# Salvando as tabelas no banco de dados com overwriteSchema habilitado
for table_name, df in dfs_consolidados.items():
    df.write.mode("overwrite").option("overwriteSchema", "true").saveAsTable(f"bronze.{table_name}")



# COMMAND ----------

# Executar comando SQL para listar as tabelas
spark.sql("SHOW TABLES IN bronze").show()

# COMMAND ----------

# MAGIC %md
# MAGIC Testando com um exemplo

# COMMAND ----------

spark.sql("DESCRIBE bronze.2020atracacao").show()

# COMMAND ----------

spark.sql("SELECT * FROM bronze.2020atracacao LIMIT 10").show()


# COMMAND ----------

# MAGIC %md
# MAGIC Unir todas as tabelas do mesmo tipo:

# COMMAND ----------

# Defina a lista de anos antes de usar
anos = ['2020', '2021', '2022', '2023', '2024']

# Verificando as chaves em dfs_consolidados
print("Tabelas carregadas em dfs_consolidados:")
print(list(dfs_consolidados.keys()))

# Dicionário para armazenar os DataFrames consolidados por tipo de tabela
dfs_por_tipo = {}

# Tipos de tabelas a serem processados
tipos_tabelas = [
    "Atracacao", "Carga_Conteinerizada", "Carga_Hidrovia", "Carga_Regiao", "Carga_Rio", 
    "TaxaOcupacao", "TaxaOcupacaoComCarga", "TaxaOcupacaoTOAtracacao", "TemposAtracacao", 
    "TemposAtracacaoParalisacao", "Carga"
]

# Loop para processar cada tipo de tabela
for tipo in tipos_tabelas:
    dfs_anos_tipo = []  # Lista para armazenar os DataFrames de todos os anos para o tipo de tabela
    
    for ano in anos:
        tabela = f"{ano}{tipo}"  # Nome da tabela para o ano e tipo
        
        # Verifica se a tabela existe no dicionário de DataFrames
        if tabela in dfs_consolidados:
            print(f"Carregando tabela: {tabela}")  # Mensagem de diagnóstico
            
            # Adiciona uma coluna "Ano" ao DataFrame antes da união
            df_com_ano = dfs_consolidados[tabela].withColumn("Ano", F.lit(ano))
            dfs_anos_tipo.append(df_com_ano)
        else:
            print(f"Tabela {tabela} não encontrada.")  # Mensagem de erro para tabela não encontrada

    # Unindo todos os anos para o tipo específico
    if dfs_anos_tipo:
        df_tipo_consolidado = dfs_anos_tipo[0]
        for df in dfs_anos_tipo[1:]:
            df_tipo_consolidado = df_tipo_consolidado.union(df)

        # Adicionando ao dicionário de DataFrames por tipo com o nome da tabela em minúsculas
        dfs_por_tipo[tipo.lower()] = df_tipo_consolidado

# Verifique os novos nomes das colunas de um DataFrame de exemplo em dfs_por_tipo
print(dfs_por_tipo[list(dfs_por_tipo.keys())[0]].columns)



# COMMAND ----------

# MAGIC %md
# MAGIC Conferir se a coluna ano foi incluída corretamente

# COMMAND ----------

dfs_por_tipo["atracacao"].select("Ano").distinct().show()


# COMMAND ----------

# MAGIC %md
# MAGIC Checar os dfs presentes em dfs_por_tipo

# COMMAND ----------

print(list(dfs_por_tipo.keys()))

# COMMAND ----------

# MAGIC %md
# MAGIC Conferir se os dfs foram carregados corretamente, utilizando um df como exemplo

# COMMAND ----------

# Supondo que você queira ver as 5 primeiras linhas de uma tabela específica dentro do dicionário
df_exemplo = dfs_por_tipo['atracacao']  
df_exemplo.head()

# COMMAND ----------

# Verificar o tipo de cada objeto
for nome_df, df in dfs_por_tipo.items():
    print(f"Objeto: {nome_df}, Tipo: {type(df)}")


# COMMAND ----------

# Iterar sobre o dicionário df_por_tipo (que contém DataFrames PySpark)
for nome_df, df in dfs_por_tipo.items():
    print(f"Objeto: {nome_df}, Tipo: {type(df)}")
    
    if isinstance(df, DataFrame):  # Verifica se é um DataFrame do PySpark
        print(f"Nome do DataFrame: {nome_df}")
        print(f"Colunas: {df.columns}")  # Listar as colunas
    else:
        print(f"O objeto {nome_df} não é um DataFrame do PySpark, tipo encontrado: {type(df)}")
    print("-" * 50)



# COMMAND ----------

# MAGIC %md
# MAGIC Criar o esquema prata

# COMMAND ----------

spark.sql("CREATE SCHEMA IF NOT EXISTS prata")


# COMMAND ----------

# Salvando as tabelas no esquema prata com overwriteSchema habilitado
for table_name, df in dfs_por_tipo.items():
    df.write.mode("overwrite").option("overwriteSchema", "true").saveAsTable(f"prata.{table_name}")

# COMMAND ----------

# MAGIC %md
# MAGIC Testar se as tabelas foram incluídas corretamente

# COMMAND ----------

spark.sql("SHOW TABLES IN prata").show()

# COMMAND ----------

# MAGIC %md
# MAGIC Verificar tipos de dados e conversões necessárias

# COMMAND ----------

tables = spark.sql("SHOW TABLES IN prata").select("tableName").collect()
tabela_lista = [t["tableName"] for t in tables]
print(tabela_lista)

# COMMAND ----------

for table in tabela_lista:
    count = spark.sql(f"SELECT COUNT(*) FROM prata.{table}").collect()[0][0]
    print(f"Tabela: {table}, Total de registros: {count}")


# COMMAND ----------

# Excluindo a tabela desnecessária no banco de dados prata
spark.sql("DROP TABLE IF EXISTS prata.atracacao_limpa")

# COMMAND ----------

# MAGIC %md
# MAGIC Verificar existência de valores nulos

# COMMAND ----------

for table in tabela_lista:
    df = spark.sql(f"SELECT * FROM prata.{table}")
    null_counts = {col: df.filter(df[col].isNull()).count() for col in df.columns}
    print(f"🔍 Tabela: {table}")
    print(f"🚨 Valores nulos por coluna: {null_counts}\n")


# COMMAND ----------

# MAGIC %md
# MAGIC Verificar existência de valores duplicados

# COMMAND ----------

for table in tabela_lista:
    # Obter os nomes das colunas da tabela
    df = spark.table(f"prata.{table}")  
    colunas = df.columns  # Lista de colunas da tabela

    if not colunas:  # Se a tabela estiver vazia, pule
        print(f"⚠️ Tabela {table} não tem colunas.")
        continue

    colunas_str = ", ".join([f"`{col}`" for col in colunas])  # Protege nomes de colunas com acentos/espaços

    # Query para contar registros duplicados
    count_duplicates = spark.sql(f"""
        SELECT COUNT(*) 
        FROM (
            SELECT {colunas_str}, COUNT(*) AS cnt 
            FROM prata.{table}
            GROUP BY {colunas_str}
            HAVING COUNT(*) > 1
        )
    """).collect()[0][0]

    print(f"🛑 Tabela: {table}, Registros duplicados: {count_duplicates}")




# COMMAND ----------

# MAGIC %md
# MAGIC Tratar dados nulos nas tabelas que possuem dados nulos

# COMMAND ----------

# Lista de tabelas para as quais queremos substituir valores nulos
tabelas_para_substituir = ["atracacao", "carga"]

for table in tabela_lista:
    df = spark.sql(f"SELECT * FROM prata.{table}")
    
    if table in tabelas_para_substituir:
        # Substituir valores nulos por "Desconhecido"
        df = df.fillna("Desconhecido")
    
    # Contar valores nulos por coluna após a substituição (deve ser 0 para todas as colunas se a substituição foi feita)
    null_counts = {col: df.filter(df[col].isNull()).count() for col in df.columns}
    
    print(f"🔍 Tabela: {table}")
    print(f"🚨 Valores nulos por coluna após substituição: {null_counts}\n")


# COMMAND ----------

# MAGIC %md
# MAGIC Tratar dados duplicados na tabela que possui dados duplicados

# COMMAND ----------

spark.sql("""
    CREATE OR REPLACE TABLE prata.carga_conteinerizada AS
    SELECT DISTINCT * 
    FROM prata.carga_conteinerizada
""")



# COMMAND ----------

# MAGIC %md
# MAGIC Conferir versão final após tratamentos

# COMMAND ----------


# Verificação das colunas
for table in tabela_lista:
    # Conta o número de registros na tabela
    count = spark.sql(f"SELECT COUNT(*) FROM prata.{table}").collect()[0][0]
    
    # Imprime o total de registros
    print(f"Tabela: {table}, Total de registros: {count}")
    
    # Listar as colunas da tabela
    columns = spark.sql(f"DESCRIBE prata.{table}").collect()  # DESCRIBE para pegar informações sobre as colunas
    print(f"Colunas da tabela {table}:")
    
    # Imprimir as colunas
    for row in columns:
        print(row['col_name'])  # A coluna 'col_name' contém os nomes das colunas

    print("-" * 50)



# COMMAND ----------

# MAGIC %md
# MAGIC Criar esquema ouro

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE SCHEMA IF NOT EXISTS ouro;
# MAGIC

# COMMAND ----------

for table in tabela_lista:
    # Carregar a tabela do esquema "prata"
    df = spark.sql(f"SELECT * FROM prata.{table}")
    
    # Salvar o DataFrame no novo esquema "ouro" com a opção overwriteSchema
    df.write.option("overwriteSchema", "true").mode("overwrite").saveAsTable(f"ouro.{table}")


# COMMAND ----------

# Verificando as tabelas do schema ouro
spark.sql("SHOW TABLES IN ouro").show()


# COMMAND ----------

# MAGIC %md
# MAGIC Verificando todas colunas de todas as tabelas

# COMMAND ----------

# Verificando as colunas da tabela ouro.atracacao
spark.sql("DESCRIBE ouro.atracacao").show()



# COMMAND ----------

# Verificando as tabelas do schema ouro
tables = spark.sql("SHOW TABLES IN ouro").collect()

# Itera sobre cada tabela e exibe as colunas
for table in tables:
    table_name = table["tableName"]
    print(f"Tabela: {table_name}")
    columns = spark.sql(f"DESCRIBE ouro.{table_name}").collect()
    for column in columns:
        print(f"Tabela: {table_name}, Coluna: {column['col_name']}, Tipo: {column['data_type']}")
    print("\n")  # Adiciona uma linha em branco para separar as tabelas

# COMMAND ----------

# Executa a consulta DESCRIBE e coleta os resultados
result = spark.sql("DESCRIBE ouro.atracacao").collect()

# Exibe todas as linhas coletadas
for row in result:
    print(row)

# COMMAND ----------

# MAGIC %md ## Realização das perguntas

# COMMAND ----------

# MAGIC %md
# MAGIC ### Qual é o tempo médio de atracação por porto?

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT 
# MAGIC     a.porto_atracacao,
# MAGIC     AVG(t.tatracado) AS tempo_medio_atracacao
# MAGIC FROM 
# MAGIC     ouro.atracacao a
# MAGIC JOIN 
# MAGIC     ouro.temposatracacao t ON a.idatracacao = t.idatracacao
# MAGIC WHERE 
# MAGIC     t.tatracado IS NOT NULL
# MAGIC GROUP BY 
# MAGIC     a.porto_atracacao
# MAGIC HAVING 
# MAGIC     AVG(t.tatracado) IS NOT NULL
# MAGIC ORDER BY 
# MAGIC     tempo_medio_atracacao DESC;

# COMMAND ----------

# MAGIC %md
# MAGIC ####Comentário:
# MAGIC O porto de São Sebastião é o porto com maior tempo médio de atracação, com 338 horas Enquanto que o Terminal Navecunha possui o menor tempo médio de atracação, com 3 horas.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Qual o volume total de carga movimentada por ano?

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT 
# MAGIC     a.Ano,
# MAGIC     SUM(c.vlpesocargabruta) AS total_carga_movimentada
# MAGIC FROM ouro.carga c
# MAGIC JOIN ouro.atracacao a ON c.idatracacao = a.idatracacao
# MAGIC GROUP BY a.Ano
# MAGIC ORDER BY a.Ano DESC;
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ####Comentário:
# MAGIC Nos últimos 5 anos, o ano com maior movimentação, em tonelada, foi 2024. Interessante perceber que o volume de carga transportada aumentou com o passar dos anos, sendo crescente de 2020 a 2024.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Qual é o total movimentado por tipo de carga?

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT 
# MAGIC     natureza_da_carga,
# MAGIC     SUM(vlpesocargabruta) AS total_movimentado
# MAGIC FROM 
# MAGIC     ouro.carga
# MAGIC GROUP BY 
# MAGIC     natureza_da_carga
# MAGIC ORDER BY total_movimentado DESC;

# COMMAND ----------

# MAGIC %md
# MAGIC ####Comentário: 
# MAGIC A Carga com maior volume transportado é Granel Sólido (grãos, minérios, cimento, sal, etc.). Esse resultado faz sentido se pensarmos na cabotagem de carga para grandes indústrias no país e na estrutura econômica do Brasil, baseada em exportação. A carga conteinerizada geralmente inclui produtos industrializados, eletrônicos e outros. Esta carga aparecer em último lugar mostra que o Brasil tem menor participação na produção e exportação desse tipo de produto.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Quais são os terminais portuários mais utilizados?

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT 
# MAGIC     terminal,
# MAGIC     COUNT(*) AS numero_atracacoes
# MAGIC FROM 
# MAGIC     ouro.atracacao
# MAGIC GROUP BY 
# MAGIC     terminal
# MAGIC ORDER BY 
# MAGIC     numero_atracacoes DESC;

# COMMAND ----------

# MAGIC %md
# MAGIC ####Comentário: 
# MAGIC Os Cais Públicos são projetados para atender uma gama maior de embarcações e tipos de carga, não surpreende estarem como os terminais com maior número de atracações.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Quais são os portos com maior número de atracações?

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT 
# MAGIC     porto_atracacao,
# MAGIC     COUNT(*) AS numero_atracacoes
# MAGIC FROM 
# MAGIC     ouro.atracacao
# MAGIC GROUP BY 
# MAGIC     porto_atracacao
# MAGIC ORDER BY 
# MAGIC     numero_atracacoes DESC;

# COMMAND ----------

# MAGIC %md
# MAGIC ####Comentário: 
# MAGIC A predominância de Belém, e região, no número de atracações se dá pela localização, uma vez que serve como ponto de entrada e saída para o comércio marítimo na Amazônia, permitindo acesso às rotas fluviais e marítimas. Além disso, o porto de Belém possui uma infraestrutura preparada para um grande número de embarcações.

# COMMAND ----------

# MAGIC %md
# MAGIC ###Quais tipos de mercadoria são mais movimentados por navegação de longo curso?

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT 
# MAGIC     c.cdmercadoria AS tipo_mercadoria,
# MAGIC     SUM(c.vlpesocargabruta) AS total_movimentado
# MAGIC FROM ouro.carga c
# MAGIC JOIN ouro.atracacao a ON c.idatracacao = a.idatracacao
# MAGIC WHERE a.tipo_de_navegacao_da_atracacao = 'Longo Curso'
# MAGIC GROUP BY c.cdmercadoria
# MAGIC ORDER BY total_movimentado DESC;

# COMMAND ----------

# MAGIC %md
# MAGIC ####Comentário: 
# MAGIC O código 2601, que lidera a lista, se refere à Minério de Ferro. Brasil é um líder na exportação de minério de ferro, e por isso, o resultado da pesquisa é coerente.

# COMMAND ----------

# MAGIC %md
# MAGIC ### Qual berço teve maior taxa de ocupação em determinado ano (ex: 2023)?

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT 
# MAGIC     idberco,
# MAGIC     SUM(tempoemminutosdias) AS TotalTempoOcupacao
# MAGIC FROM 
# MAGIC     ouro.taxaocupacao
# MAGIC WHERE 
# MAGIC     anotaxaocupacao = '2023'
# MAGIC GROUP BY 
# MAGIC     idberco
# MAGIC ORDER BY 
# MAGIC     TotalTempoOcupacao DESC
# MAGIC LIMIT 1;

# COMMAND ----------

# MAGIC %md
# MAGIC Testando a pesquisa para anos específicos

# COMMAND ----------

# MAGIC %md
# MAGIC ### Qual o tempo médio de viagem por tipo de navio?

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT 
# MAGIC     a.tipo_de_navegacao_da_atracacao AS TipoNavio,
# MAGIC     AVG(t.testadia) AS TempoMedioViagem
# MAGIC FROM 
# MAGIC     ouro.temposatracacao t
# MAGIC JOIN 
# MAGIC     ouro.atracacao a ON t.idatracacao = a.idatracacao
# MAGIC WHERE 
# MAGIC     a.tipo_de_navegacao_da_atracacao IS NOT NULL
# MAGIC GROUP BY 
# MAGIC     a.tipo_de_navegacao_da_atracacao
# MAGIC ORDER BY TempoMedioViagem DESC;

# COMMAND ----------

# MAGIC %md
# MAGIC ####Comentário: 
# MAGIC Era de se esperar que o tempo de viagem do tipo de navegação Longo Curso fosse maior do que as outras pela própria natureza da navegação. Porém, as embarcações de apoio portuário, como rebocadores, lanchas de serviço e embarcações de abastecimento, têm funções específicas que podem exigir longos períodos de operação até fechar a viagem.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Autoavaliação
# MAGIC
# MAGIC Durante o desenvolvimento deste MVP, pude aprofundar meus conhecimentos, tendo sido a primeira vez construindo um pipeline em nuvem. Um dos principais aprendizados foi a importância da padronização e limpeza dos dados desde o início do processo, o que se mostrou fundamental para a consistência das análises e a usabilidade futura via SQL.
# MAGIC
# MAGIC Minha maior dificuldade foi no entendimento da nova linguagem, e em lidar com o desafio da ocorrência de erros consecutivos que eu achava já ter resolvido. Um deles foi em relação aos caracteres especiais no nome das tabelas e nome das colunas que foi um erro persistente durante todo o projeto até que eu conseguisse resolver.
# MAGIC
# MAGIC O exercício de pensar em perguntas utilizando as diferentes tabelas foi interessante, sendo obrigada a realmente entender que tipo de dado eu tinha. 
# MAGIC
# MAGIC Como pontos de melhoria, vejo que preciso me dedicar e mergulhar mais em SQL, e na construção das relações entre as tabelas. Ter utilizado tabelas printas, disponibilizadas por órgão de confiança, foi um facilitador no processo, e mesmo assim tive dificuldades. 

# COMMAND ----------

