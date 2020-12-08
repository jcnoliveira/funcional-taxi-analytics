# Funcional-Taxi Analytics


## Projeto - Ambiente de extração de dados do Twitter

Essa é uma arquitetura que importa dados do S3 para uma instancia de Redshift, ulizando a instrução COPY.
Toda a parte de credenciais está dinamica, ou seja, sem senhas fixas, utilizando o Secrets Manager como fonte de autenticação.
A arquitetura de armazenamento foi projetada na AWS, já a camada de Data Visualization foi feita local.


## Documentação de arquitetura

![Arquitetura](https://github.com/jcnoliveira/funcional-taxi-analytics/blob/main/Images/funcional.png)


1. Lambda Function

Função Lambda em python responsabel por realizar a ingestão de dados no RedShift e criação das tabelas.

2. Redshift

Dataware house que faz a ingestão das 4MM de linhas em 50 segundos. Nesse exemplo, utilizamos apenas 1 nó.

3. S3

Storage de objetos que armazena os dados que serão ingeridos pelo Redshift.

4. Secrets Manager

Serviço responsavel por armazenar e fornecer, de modo seguro, as credenciais do ambiente.

5. Metabase

Ferramenta de data visualization.


## Arquivos

##### cf.yaml

Arquivo com o cloudformation do projeto. Detalhes da utilização na proxima parte.

##### queries.sql

Arquivo com as queries SQL utilizadas para obter as informações solicitadas. Foram utilizadas no metabase para gerar os relatorios.

##### Personal - NYC Taxi Analytics · Dashboard · Metabase.pdf

Arquivo com o dashboard extraido do metabase com os gráficos.

##### dataimport.py, conn.py e log.py

Arquivos python que serão executados no lambda.


## Rollout! Implantação

1. Nesse momento, a subida do zip do lambda ainda não está automatizada.