# Catálogo de Dados
Este README fornece uma visão geral das tabelas e suas colunas, facilitando a compreensão dos dados armazenados e suas respectivas descrições.

## Tabela: atracacao

### Descrição
A tabela `atracacao` contém informações detalhadas sobre as atracações de embarcações em portos brasileiros. Cada registro representa uma atracação específica, incluindo detalhes sobre o porto, berço, datas e tipos de operações.

### Estrutura da Tabela

| Atributo                      | Descrição                                                                                                                                                                                                 |
|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `IDAtracacao`                 | Código de identificação da atracação.                                                                                                                                                                      |
| `CDTUP`                       | Código de identificação do porto informante (Porto Público: Bigrama+Trigrama; Porto Privado: Código da Antaq - BR+UF+xxx), disponível para consulta na página: [web.antaq.gov.br](http://web.antaq.gov.br/portalv3/sdpv2servicosonline/ConsultarPorto.aspx). |
| `IDBerco`                     | Código de identificação do berço do porto informante.                                                                                                                                                      |
| `Berço`                       | Nome do berço do porto informante. Local da atracação (berço) do porto informante, cadastrado previamente na base da Antaq. Códigos de berços disponíveis para consulta na página: [web.antaq.gov.br](http://web.antaq.gov.br/portalv3/sdpv2servicosonline/ConsultarBerco.aspx). |
| `Porto Atracação`             | Nome do porto informante.                                                                                                                                                                                  |
| `Coordenadas`                 | Latitude e longitude do porto informante em Graus Decimais (DD, em inglês).                                                                                                                                 |
| `Apelido Instalação Portuária`| Apelido do porto informante.                                                                                                                                                                               |
| `Complexo Portuário`          | Complexo Portuário do porto informante.                                                                                                                                                                    |
| `Tipo da Autoridade Portuária`| Tipo de autoridade portuária do porto informante, que pode ser Porto Público ou Porto Privado.                                                                                                              |
| `Data Atracação`              | Data e hora de atracação da embarcação no porto (yyyy-MM-dd hh:mm:ss).                                                                                                                                     |
| `Data Chegada`                | Data e hora de chegada da embarcação no porto (yyyy-MM-dd hh:mm:ss).                                                                                                                                       |
| `Data Desatracação`           | Data e hora de desatracação da embarcação no porto (yyyy-MM-dd hh:mm:ss).                                                                                                                                  |
| `Data Início Operação`        | Data e hora de início da Operação (yyyy-MM-dd hh:mm:ss).                                                                                                                                                   |
| `Data Término Operação`       | Data e hora de término da operação (yyyy-MM-dd hh:mm:ss).                                                                                                                                                  |
| `Tipo de Operação`            | Tipo de operação (finalidade) da atracação: Movimentação da Carga (1), Passageiro (2), Apoio (3), Marinha (4), Abastecimento (5), Reparo/Manutenção (6), Misto (7) ou Retirada de Resíduos (8).              |
| `Tipo de Navegação da Atracação`| Tipo de navegação da embarcação: Navegação Interior (1), Apoio Portuário (2), Cabotagem (3), Apoio Marítimo (4) ou Longo Curso (5).                                                                        |
| `Nacionalidade do Armador`    | Nacionalidade Armador: Brasileira (1) e Estrangeira (2).                                                                                                                                                   |
| `FlagMCOperacaoAtracacao`     | Se for igual a 1, identifica que a atracação é contabilizada como movimentação de carga.                                                                                                                    |
| `Terminal`                    | Se o tipo de autoridade portuária do porto informante for Porto Público, será informado o terminal arrendado ou público onde ocorreu a atracação.                                                           |
| `Município`                   | Município do porto informante.                                                                                                                                                                             |
| `UF`                          | Nome da unidade da federação do porto informante.                                                                                                                                                          |
| `SGUF`                        | Sigla da unidade da federação do porto informante.                                                                                                                                                          |
| `Região Geográfica`           | Nome da região geográfica do porto informante.                                                                                                                                                             |
| `Região Hidrográfica`         | Nome da região hidrográfica do porto informante.                                                                                                                                                           |
| `Instalação Portuária em Rio` | Identifica com valor Sim, se o porto informante está localizado em um rio brasileiro, e Não, caso não esteja localizado em rio brasileiro.                                                                 |
| `Nº da Capitania`             | Código atribuído pela Capitania dos Portos do Brasil. Utilizado quando a embarcação não possuir número IMO.                                                                                                 |
| `Nº do IMO`                   | Número da International Maritime Organization (IMO) atribuído à embarcação.                                                                                                                                 |

### Observações
- Os códigos de identificação do porto e do berço podem ser consultados nas páginas da Antaq fornecidas nas descrições.
- As datas e horas são registradas no formato `yyyy-MM-dd hh:mm:ss`.
- Os tipos de operação e navegação são representados por números, conforme descrito na tabela.


## Tabela: carga

### Descrição
A tabela `carga` contém informações detalhadas sobre as cargas movimentadas em portos brasileiros. Cada registro representa uma carga específica, incluindo detalhes sobre a origem, destino, tipo de mercadoria, e características da operação.

### Estrutura da Tabela

| Atributo                          | Descrição                                                                                                                                                                                                 |
|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `IDCarga`                         | Código de identificação da carga.                                                                                                                                                                         |
| `IDAtracacao`                     | Código de identificação da atracação. Ligação com a tabela de atracação.                                                                                                                                   |
| `Origem`                          | Código do porto de origem da carga (porto de embarque), disponível para consulta na página: [web.antaq.gov.br](http://web.antaq.gov.br/portalv3/sdpv2servicosonline/ConsultarPorto.aspx).                  |
| `Destino`                         | Código do porto de destino da carga (porto de desembarque), disponível para consulta na página: [web.antaq.gov.br](http://web.antaq.gov.br/portalv3/sdpv2servicosonline/ConsultarPorto.aspx).                |
| `CDMercadoria`                    | Classificação Nomenclatura Comum do Mercosul (código NCM SH4) para mercadorias. Contém os quatro primeiros dígitos do código NCM referente à posição do Sistema Harmonizado (SH). Contêineres e semireboques baú devem ser informados neste campo, por meio de códigos próprios. Códigos de mercadoria disponíveis para consulta na página: [web.antaq.gov.br](http://web.antaq.gov.br/portalv3/sdpv2servicosonline/ConsultarMercadoria.aspx). |
| `Tipo Operação da Carga`          | Classificação do tipo de operação da carga. Classificado até março de 2018 como: Apoio, Transbordo e Movimentação de Carga. A partir de abril de 2018, classificado de acordo com a Instrução Normativa 800 da Receita Federal, de 27 de dezembro de 2007. |
| `Carga Geral Acondicionamento`    | Classifica a carga geral como solta ou conteinerizada.                                                                                                                                                    |
| `ConteinerEstado`                 | Situação de preenchimento do contêiner, com valores possíveis de cheio (C) ou vazio (V).                                                                                                                  |
| `Tipo Navegação`                  | Tipo de navegação da carga, de acordo com os portos de embarque e desembarque: Navegação Interior (1), Apoio Portuário (2), Cabotagem (3), Apoio Marítimo (4) ou Longo Curso (5).                          |
| `FlagAutorizacao`                 | Identifica o transporte na navegação interior que utiliza portos públicos e privados autorizados pela Antaq. Dessa forma, podem ser considerados ou não os dados provenientes das administrações hidroviárias e demais fontes de informação, que não estão no Sistema Desempenho Portuário - SDP. |
| `FlagCabotagem`                   | Diferencia os montantes transportados na navegação de cabotagem daqueles movimentados pelos portos. Isto é, por conta de ser uma navegação doméstica, o transporte de cabotagem gera movimentação portuária na origem e no destino da carga, e essa flag evita a dupla contagem para fins de transporte. |
| `FlagCabotagemMovimentacao`       | Diferencia os montantes movimentados na navegação de cabotagem. Isto é, considera para fins de apuração a movimentação portuária gerada na origem e destino do transporte em navegação de cabotagem.        |
| `FlagConteinerTamanho`            | Categoriza os diversos tamanhos de contêiner em 20', 40' ou outros.                                                                                                                                       |
| `FlagLongoCurso`                  | Identifica o transporte e a movimentação de cargas na navegação de longo curso.                                                                                                                            |
| `FlagMCOperacaoCarga`             | Identifica os tipos de operação de carga que serão considerados para fins de apuração de movimentação e transporte.                                                                                        |
| `FlagOffshore`                    | Identifica as cargas oriundas de bacias sedimentares ou plataformas marítimas.                                                                                                                             |
| `FlagTransporteViaInterioir`      | Identifica que o transporte ocorreu em via interior.                                                                                                                                                      |
| `Percurso Transporte em vias Interiores` | Classifica o percurso de transporte realizado exclusivamente em vias interiores. Podendo ser via Interior Internacional, Interior Estadual, Interior Interestadual ou Interior de percurso não identificado. |
| `Percurso Transporte Interiores`  | Compreende a navegação que utilizou uma via interior no todo ou em parte do percurso de transporte. É classificada em longo curso em vias interiores, cabotagem em vias interiores e navegação interior.   |
| `STNaturezaCarga`                 | Identificação que na atracação foi somente movimentada uma única natureza de carga. Utilizado para o cálculo de produtividade por grupo de mercadoria. Pode ser: Exclusivo ou compartilhado.                |
| `STSH2`                           | Identificação que na atracação foi somente movimentada um único capítulo. Utilizado para o cálculo de produtividade por grupo de mercadoria. Pode ser: Exclusivo ou compartilhado.                         |
| `STSH4`                           | Identificação que na atracação foi somente movimentada uma única mercadoria. Utilizado para o cálculo de produtividade por mercadoria. Pode ser: Exclusivo ou compartilhado.                              |
| `Natureza da Carga`               | Natureza da carga: Granel Sólido, Granel Líquido, Carga Geral ou Carga Conteinerizada.                                                                                                                     |
| `Sentido`                         | Sentido da Operação: Desembarque (1) ou Embarque (2).                                                                                                                                                     |
| `TEU`                             | Se natureza da carga for contêiner, quantidade movimentada em TEUs (Twenty-foot Equivalent Unit).                                                                                                          |
| `QTCarga`                         | Quantidade movimentada em unidades, se código carga referente a Contêineres ou Automóveis.                                                                                                                 |
| `VLPesoCargaBruta`                | Peso bruto da carga, em toneladas. Para contêineres cheios: peso da tara do contêiner somado ao peso da carga acondicionada, em toneladas.                                                                |

### Observações
- Os códigos de identificação do porto de origem e destino podem ser consultados nas páginas da Antaq fornecidas nas descrições.
- As classificações de mercadorias podem ser consultadas na página da Antaq fornecida na descrição.
- As flags (indicadores) são usadas para diferenciar e categorizar diferentes aspectos do transporte e movimentação de cargas.


## Tabela: carga_conteinerizada

### Descrição
A tabela `carga_conteinerizada` contém informações detalhadas sobre as cargas conteinerizadas movimentadas em portos brasileiros. Cada registro representa uma carga específica dentro de um contêiner, incluindo detalhes sobre a classificação da mercadoria e o peso líquido.

### Estrutura da Tabela

| Atributo                      | Descrição                                                                                                                                                                                                 |
|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `IDCarga`                     | Código de identificação da carga. Ligação com a tabela de carga.                                                                                                                                           |
| `CDMercadoriaConteinerizada`  | Classificação Nomenclatura Comum do Mercosul (código NCM SH4) para mercadorias informadas dentro do contêiner. Contém os quatro primeiros dígitos do código do NCM referente à posição do Sistema Harmonizado (SH). Códigos de mercadoria disponíveis para consulta na página: [web.antaq.gov.br](http://web.antaq.gov.br/portalv3/sdpv2servicosonline/ConsultarMercadoria.aspx). |
| `VLPesoCargaConteinerizada`   | Peso líquido da carga conteinerizada, em toneladas.                                                                                                                                                        |

### Observações
- Os códigos de classificação das mercadorias podem ser consultados na página da Antaq fornecida na descrição.
- A tabela `carga_conteinerizada` está relacionada à tabela `carga` através do atributo `IDCarga`.


## Tabela: carga_hidrovia

### Descrição
A tabela `carga_hidrovia` contém informações detalhadas sobre as cargas transportadas por hidrovias em portos brasileiros. Cada registro representa uma carga específica transportada por uma hidrovia, incluindo detalhes sobre a hidrovia e o peso transportado.

### Estrutura da Tabela

| Atributo          | Descrição                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------|
| `IDCarga`         | Código de identificação da carga. Ligação com a tabela de carga.                                 |
| `Hidrovia`        | Nome da hidrovia onde foi realizado o transporte de carga.                                       |
| `ValorMovimentado`| Peso transportado em toneladas.                                                                 |

### Observações
- A tabela `carga_hidrovia` está relacionada à tabela `carga` através do atributo `IDCarga`.


## Tabela: carga_regiao

### Descrição
A tabela `carga_regiao` contém informações detalhadas sobre as cargas transportadas por regiões hidrográficas em portos brasileiros. Cada registro representa uma carga específica transportada por uma região hidrográfica, incluindo detalhes sobre a região e o peso transportado.

### Estrutura da Tabela

| Atributo              | Descrição                                                                                       |
|-----------------------|-------------------------------------------------------------------------------------------------|
| `IDCarga`             | Código de identificação da carga. Ligação com a tabela de carga.                                 |
| `Região Hidrográfica` | Nome da região hidrográfica onde foi realizado o transporte de carga.                            |
| `ValorMovimentado`    | Peso transportado em toneladas.                                                                 |

### Observações
- A tabela `carga_regiao` está relacionada à tabela `carga` através do atributo `IDCarga`.



## Tabela: carga_rio

### Descrição
A tabela `carga_rio` contém informações detalhadas sobre as cargas transportadas por rios em portos brasileiros. Cada registro representa uma carga específica transportada por um rio, incluindo detalhes sobre o rio e o peso transportado.

### Estrutura da Tabela

| Atributo          | Descrição                                                                                       |
|-------------------|-------------------------------------------------------------------------------------------------|
| `IDCarga`         | Código de identificação da carga. Ligação com a tabela de carga.                                 |
| `Rio`             | Nome do rio onde foi realizado o transporte de carga.                                            |
| `ValorMovimentado`| Peso transportado em toneladas.                                                                 |

### Observações
- A tabela `carga_rio` está relacionada à tabela `carga` através do atributo `IDCarga`.


## Tabela: destino_carga

### Descrição
A tabela `destino_carga` contém informações detalhadas sobre os portos de destino das cargas movimentadas em portos brasileiros. Cada registro representa um destino específico, incluindo detalhes sobre o porto, localização geográfica e classificações econômicas.

### Estrutura da Tabela

| Atributo                   | Descrição                                                                                                                                                                                                 |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Destino`                  | Código do porto de destino da carga (porto de desembarque). Ligação com a tabela de carga. Disponível para consulta na página: [web.antaq.gov.br](http://web.antaq.gov.br/portalv3/sdpv2servicosonline/ConsultarPorto.aspx). |
| `Nome Destino`             | Nome do porto de destino da carga, segundo tabela disponível para consulta na página: [web.antaq.gov.br](http://web.antaq.gov.br/portalv3/sdpv2servicosonline/ConsultarPorto.aspx).                        |
| `CDBigramaDestino`         | Código bigrama do país do porto de destino da carga, segundo tabela disponível para consulta na página: [web.antaq.gov.br](http://web.antaq.gov.br/portalv3/sdpv2servicosonline/ConsultarPorto.aspx).        |
| `CDTrigramaDestino`        | Se porto público ou internacional, código trigrama do país do porto de destino da carga, segundo tabela disponível para consulta na página: [web.antaq.gov.br](http://web.antaq.gov.br/portalv3/sdpv2servicosonline/ConsultarPorto.aspx). |
| `CDTUPDestino`             | Utilizado para porto privado, código da instalação portuária de destino da carga, segundo tabela disponível para consulta na página: [web.antaq.gov.br](http://web.antaq.gov.br/portalv3/sdpv2servicosonline/ConsultarInstalacaoPortuaria.aspx). |
| `Rio Destino`              | Se porto for fluvial, nome do rio onde está o porto. Não se aplica a portos marítimos.                                                                                                                     |
| `Região Hidrográfica Destino` | Nome da região hidrográfica do porto de destino da carga. Não se aplica a portos marítimos.                                                                                                               |
| `UF.Destino`               | Sigla da UF do porto de destino da carga.                                                                                                                                                                  |
| `Cidade Destino`           | Nome da cidade do porto de destino da carga. Se o porto de país estrangeiro, atributo preenchido com hífen (-).                                                                                            |
| `País Destino`             | Nome do país do porto de destino da carga.                                                                                                                                                                 |
| `Continente Destino`       | Nome do continente do porto de destino da carga.                                                                                                                                                           |
| `BlocoEconomico_Destino`   | Nome do bloco econômico do porto de destino da carga.                                                                                                                                                      |

### Observações
- Os códigos de identificação do porto de destino podem ser consultados nas páginas da Antaq fornecidas nas descrições.
- A tabela `destino_carga` está relacionada à tabela `carga` através do atributo `Destino`.


## Tabela: origem_carga

### Descrição
A tabela `origem_carga` contém informações detalhadas sobre os portos de origem das cargas movimentadas em portos brasileiros. Cada registro representa uma origem específica, incluindo detalhes sobre o porto, localização geográfica e classificações econômicas.

### Estrutura da Tabela

| Atributo                   | Descrição                                                                                                                                                                                                 |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `Origem`                   | Código do porto de origem da carga (porto de embarque). Ligação com a tabela de carga. Disponível para consulta na página: [web.antaq.gov.br](http://web.antaq.gov.br/portalv3/sdpv2servicosonline/ConsultarPorto.aspx). |
| `Origem Nome`              | Nome do porto de origem da carga, segundo tabela disponível para consulta na página: [web.antaq.gov.br](http://web.antaq.gov.br/portalv3/sdpv2servicosonline/ConsultarPorto.aspx).                        |
| `CDBigramaOrigem`          | Código bigrama do país do porto de origem da carga, segundo tabela disponível para consulta na página: [web.antaq.gov.br](http://web.antaq.gov.br/portalv3/sdpv2servicosonline/ConsultarPorto.aspx).        |
| `CDTrigramaOrigem`         | Se porto público ou internacional, código trigrama do país do porto de origem da carga, segundo tabela disponível para consulta na página: [web.antaq.gov.br](http://web.antaq.gov.br/portalv3/sdpv2servicosonline/ConsultarPorto.aspx). |
| `CDTUPOrigem`              | Utilizado para porto privado, código da instalação portuária de origem da carga, segundo tabela disponível para consulta na página: [web.antaq.gov.br](http://web.antaq.gov.br/portalv3/sdpv2servicosonline/ConsultarInstalacaoPortuaria.aspx). |
| `Rio Origem`               | Se porto for fluvial, nome do rio onde está o porto. Não se aplica a portos marítimos.                                                                                                                     |
| `Região Hidrográfica Origem` | Nome da região hidrográfica do porto de origem da carga. Não se aplica a portos marítimos.                                                                                                               |
| `UF.Origem`                | Sigla da UF do porto de origem da carga.                                                                                                                                                                  |
| `Cidade Origem`            | Nome da cidade do porto de origem da carga. Se o porto de país estrangeiro, atributo preenchido com hífen (-).                                                                                            |
| `País Origem`              | Nome do país do porto de origem da carga.                                                                                                                                                                 |
| `Continente Origem`        | Nome do continente do porto de origem da carga.                                                                                                                                                           |
| `BlocoEconomico_Origem`    | Nome do bloco econômico do porto de origem da carga.                                                                                                                                                      |

### Observações
- Os códigos de identificação do porto de origem podem ser consultados nas páginas da Antaq fornecidas nas descrições.
- A tabela `origem_carga` está relacionada à tabela `carga` através do atributo `Origem`.


## Tabela: mercadoria

### Descrição
A tabela `mercadoria` contém informações detalhadas sobre as mercadorias movimentadas em portos brasileiros. Cada registro representa uma mercadoria específica, incluindo detalhes sobre sua classificação na Nomenclatura Comum do Mercosul (NCM), tipo de contêiner, e nomenclatura simplificada.

### Estrutura da Tabela

| Atributo                          | Descrição                                                                                                                                                                                                 |
|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CDMercadoria`                    | Classifica, por meio da Nomenclatura Comum do Mercosul (código NCM SH4), as mercadorias movimentadas. Contém os quatro primeiros dígitos do código NCM. Ligação com a tabela de carga. Contêineres e semireboques baú devem ser informados neste campo, por meio de códigos próprios. Códigos de mercadoria disponíveis para consulta na página: [web.antaq.gov.br](http://web.antaq.gov.br/portalv3/sdpv2servicosonline/ConsultarMercadoria.aspx). |
| `CDNCMSH2`                        | Classificação Nomenclatura Comum do Mercosul (código NCM SH2) para mercadorias. Contém os 2 primeiros dígitos do código NCM.                                                                                 |
| `Tipo Conteiner`                  | Se a natureza da carga for conteinerizada, contém o tipo do contêiner. Senão, não é preenchido.                                                                                                             |
| `Grupo de Mercadoria`             | Nome do Capítulo da Nomenclatura Comum do Mercosul (NCM SH2) para mercadoria.                                                                                                                               |
| `Mercadoria`                      | Nome da posição da Nomenclatura Comum do Mercosul (NCM SH4) para mercadoria.                                                                                                                                |
| `Nomenclatura Simplificada Mercadoria` | Nomenclatura para conjunto de mercadorias. Elaborado pela Antaq para facilitar as pesquisas pelos usuários.                                                                                                 |

### Observações
- Os códigos de classificação das mercadorias podem ser consultados na página da Antaq fornecida na descrição.
- A tabela `mercadoria` está relacionada à tabela `carga` através do atributo `CDMercadoria`.


## Tabela: mercadoria_conteinerizada

### Descrição
A tabela `mercadoria_conteinerizada` contém informações detalhadas sobre as mercadorias movimentadas em contêineres nos portos brasileiros. Cada registro representa uma mercadoria específica dentro de um contêiner, incluindo detalhes sobre sua classificação na Nomenclatura Comum do Mercosul (NCM) e nomenclatura simplificada.

### Estrutura da Tabela

| Atributo                                      | Descrição                                                                                                                                                                                                 |
|-----------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `CDMercadoriaConteinerizada`                  | Classifica, por meio da Nomenclatura Comum do Mercosul (código NCM SH4), as mercadorias movimentadas em contêineres. Contém os quatro primeiros dígitos do código NCM. Ligação com a tabela de carga conteinerizada. Contêineres e semireboques baú devem ser informados neste campo, por meio de códigos próprios. Códigos de mercadoria disponíveis para consulta na página: [web.antaq.gov.br](http://web.antaq.gov.br/portalv3/sdpv2servicosonline/ConsultarMercadoria.aspx). |
| `CDGrupoMercadoriaConteinerizada`             | Classificação Nomenclatura Comum do Mercosul (código NCM SH2) para mercadorias. Contém os 2 primeiros dígitos do código NCM.                                                                                 |
| `Grupo Mercadoria Conteinerizada`             | Nome do Capítulo da Nomenclatura Comum do Mercosul (NCM SH2) para mercadoria.                                                                                                                               |
| `Mercadoria Conteinerizada`                   | Nome da posição da Nomenclatura Comum do Mercosul (NCM SH4) para mercadoria.                                                                                                                                |
| `Nomenclatura Simplificada Mercadoria Conteinerizada` | Nomenclatura para conjunto de mercadorias. Elaborado pela Antaq para facilitar as pesquisas pelos usuários.                                                                                                 |

### Observações
- Os códigos de classificação das mercadorias podem ser consultados na página da Antaq fornecida na descrição.
- A tabela `mercadoria_conteinerizada` está relacionada à tabela `carga_conteinerizada` através do atributo `CDMercadoriaConteinerizada`.


## Tabela: taxaocupacao

### Descrição
A tabela `taxaocupacao` contém informações detalhadas sobre a ocupação dos berços nos portos brasileiros. Cada registro representa a ocupação de um berço em um dia específico, incluindo detalhes sobre o tempo de ocupação em minutos.

### Estrutura da Tabela

| Atributo            | Descrição                                                                                       |
|---------------------|-------------------------------------------------------------------------------------------------|
| `IDBerco`           | Código de identificação do berço do porto informante.                                           |
| `DiaTaxaOcupacao`   | Dia de ocupação do berço.                                                                       |
| `MêsTaxaOcupacao`   | Mês de ocupação do berço.                                                                       |
| `AnoTaxaOcupacao`   | Ano de ocupação do berço.                                                                       |
| `TempoEmMinutosdias`| Tempo em minutos do dia com o berço ocupado para todos os tipos de operação da atracação.       |

### Observações
- A tabela `taxaocupacao` fornece uma visão detalhada da ocupação dos berços, permitindo análises sobre a utilização dos recursos portuários ao longo do tempo.



## Tabela: taxaocupacaocomcarga

### Descrição
A tabela `taxaocupacaocomcarga` contém informações detalhadas sobre a ocupação dos berços nos portos brasileiros, especificamente para os tipos de operação da atracação com carga. Cada registro representa a ocupação de um berço em um dia específico, incluindo detalhes sobre o tempo de ocupação em minutos para operações com carga.

### Estrutura da Tabela

| Atributo                      | Descrição                                                                                                                                                                                                 |
|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `IDBerco`                     | Código de identificação do berço do porto informante.                                                                                                                                                      |
| `DiaTaxaOcupacao`             | Dia de ocupação do berço.                                                                                                                                                                                  |
| `MêsTaxaOcupacao`             | Mês de ocupação do berço.                                                                                                                                                                                  |
| `AnoTaxaOcupacao`             | Ano de ocupação do berço.                                                                                                                                                                                  |
| `TempoEmMinutosdiasFlagCarga` | Tempo em minutos do dia com o berço ocupado para os tipos de operação da atracação com carga (tipo de operação de carga: Movimentação de Carga, Apoio, Transbordo, Longo Curso Exportação, Longo Curso Importação, Longo Curso Exportação com Baldeação de Carga Estrangeira, Longo Curso Importação com Baldeação de Carga Estrangeira, Cabotagem, Interior, Baldeação de Carga Nacional e Baldeação de Carga Estrangeira de Passagem). |

### Observações
- A tabela `taxaocupacaocomcarga` fornece uma visão detalhada da ocupação dos berços para operações com carga, permitindo análises sobre a utilização dos recursos portuários para diferentes tipos de operações de carga ao longo do tempo.



## Tabela: taxaocupacaotoatracacao

### Descrição
A tabela `taxaocupacaotoatracacao` contém informações detalhadas sobre a ocupação dos berços nos portos brasileiros, especificando o tempo de ocupação para cada tipo de operação da atracação. Cada registro representa a ocupação de um berço em um dia específico, incluindo detalhes sobre o tempo de ocupação em minutos para diferentes finalidades de atracação.

### Estrutura da Tabela

| Atributo                              | Descrição                                                                                                                                                                                                 |
|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `IDBerco`                             | Código de identificação do berço do porto informante.                                                                                                                                                      |
| `DSTipoOperacaoAtracacaoTaxaOcupacao` | Tipo de operação (finalidade) da atracação: Movimentação da Carga, Apoio, Marinha, Abastecimento, Reparo/Manutenção, Misto ou Retirada de Resíduos.                                                         |
| `DiaTaxaOcupacao`                     | Dia de ocupação do berço.                                                                                                                                                                                  |
| `MêsTaxaOcupacao`                     | Mês de ocupação do berço.                                                                                                                                                                                  |
| `AnoTaxaOcupacao`                     | Ano de ocupação do berço.                                                                                                                                                                                  |
| `TempoEmMinutosdiasTOAtracacao`       | Tempo em minutos do dia com o berço ocupado para cada tipo de operação da atracação.                                                                                                                        |

### Observações
- A tabela `taxaocupacaotoatracacao` fornece uma visão detalhada da ocupação dos berços para diferentes tipos de operações de atracação, permitindo análises sobre a utilização dos recursos portuários para diversas finalidades ao longo do tempo.



## Tabela: temposatracacao

### Descrição
A tabela `temposatracacao` contém informações detalhadas sobre os tempos de espera e operação das atracações de navios em portos brasileiros. Cada registro representa uma atracação específica, incluindo detalhes sobre os diferentes tempos medidos em horas.

### Estrutura da Tabela

| Atributo              | Descrição                                                                                                                                                                                                 |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `IDAtracacao`         | Código de identificação da atracação. Ligação com a tabela de atracação.                                                                                                                                   |
| `TEsperaAtracacao`    | T1 (horas) - É definido como sendo a diferença entre a data/hora de atracação do navio e a data/hora de chegada do mesmo à área de fundeio. Inclui o tempo de viagem pelo canal de acesso e eventual tempo de espera para atracação do navio. |
| `TEsperaInicioOp`     | T2 (horas) - É definido como sendo a diferença entre a data/hora de início de operação do navio e a data/hora de atracação deste. Trata-se do tempo em que o navio, já atracado, espera para que se inicie a operação de carga/descarga. |
| `TOperacao`           | T3 (horas) - É definido como sendo a diferença entre a data/hora de término da operação do navio e a data/hora de início dessa operação. Este é o tempo que se usa para calcular a Prancha Média Operacional (PMO). |
| `TEsperaDesatracacao` | T4 (horas) - É definido como sendo a diferença entre a data/hora de desatracação do navio e a data/hora de término da operação. Trata-se do tempo em que o navio aguarda no berço até a sua desatracação, para iniciar a viagem de saída da instalação portuária. |
| `TAtracado`           | TA (horas) - É definido como a soma de todos os tempos onde a embarcação permaneceu no berço da instalação portuária, ou seja, TA = T2 + T3 + T4. Este é o tempo que se usa para calcular a Prancha Média Geral (PMG). |
| `TEstadia`            | TE (horas) - É definido como a soma de todos os tempos desde a chegada do navio na área de fundeio até a sua desatracação do berço, ou seja, TE = T1 + T2 + T3 + T4. |

### Observações
- A tabela `temposatracacao` fornece uma visão detalhada dos diferentes tempos envolvidos nas operações de atracação, permitindo análises sobre a eficiência e utilização dos recursos portuários.
- Os tempos são medidos em horas e são utilizados para calcular métricas importantes como a Prancha Média Operacional (PMO) e a Prancha Média Geral (PMG).



## Tabela: temposatracacaoparalisacao

### Descrição
A tabela `temposatracacaoparalisacao` contém informações detalhadas sobre os tempos de paralisação das atracações de navios em portos brasileiros. Cada registro representa um período de paralisação específico, incluindo detalhes sobre o motivo e as datas de início e término da paralisação.

### Estrutura da Tabela

| Atributo               | Descrição                                                                                       |
|------------------------|-------------------------------------------------------------------------------------------------|
| `IDTemposDescontos`    | Código sequencial de identificação do tempo de paralisação da atracação.                        |
| `IDAtracacao`          | Código de identificação da atracação.                                                           |
| `DescricaoTempoDesconto` | Descrição do motivo do tempo de paralisação da atracação.                                      |
| `DTInicio`             | Data e hora de início da paralisação da atracação (yyyy-MM-dd hh:mm:ss).                        |
| `DTTermino`            | Data e hora de término da paralisação da atracação (yyyy-MM-dd hh:mm:ss).                       |

##3 Observações
- A tabela `temposatracacaoparalisacao` fornece uma visão detalhada dos períodos de paralisação das atracações, permitindo análises sobre os motivos e durações das paralisações.
- As datas e horas são registradas no formato `yyyy-MM-dd hh:mm:ss`.
