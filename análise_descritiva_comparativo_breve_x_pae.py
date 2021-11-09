# -*- coding: utf-8 -*-
"""Análise Descritiva - Comparativo Breve x PAE.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LOoV4tPoGHV7X2UQaoXZON_GDCpha1hK

#Comparação de Desempenho dos Processos de Negócio - Breve e PAE

Este estudo tem por objetivo identificar se houve ganho de desempenho na execução de processos administrativos a partir da adoção de um novo sistema que teve como premissa o otimização e automação dos processos de negócio de um órgão do Poder Judiciário Federal

Esta análise levou em consideração três indicadores de desempenho:

*   **Tempo total**: Tempo decorrido em dias do início ao encerramento do processo
*   **Quantidade de tramitações**: Número de tramitações entre as unidades organizacionais realizadas durante a tramitação do processo
*   **Tempo médio de tramitação**: Tempo médio em que o processo fica sendo analisado pelas unidades organizacionais.

##Importação das Bibliotecas
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

"""##Carga e Preparação dos Dados do Breve"""

dados_breve = pd.read_excel('/content/drive/MyDrive/Colab Notebooks/Dados/DS - Processo ADM/dados.breve.xlsx')

dados_breve.columns = ['ID', 'NOME_PROCESSO', 'UNIDADE_ORIGEM', 'USUARIO_ORIGEM', 'DATA_INICIO', 'DATA_FIM', 'TEMPO_TOTAL', 'QUANTIDADE_TRAMITACOES', 'TEMPO_MEDIO_TRAMITACAO', 'NOME_SISTEMA', 'ANO', 'NOME_PROCESSO_PAE']

dados_breve.describe()

dados_breve['NOME_PROCESSO'].unique()

"""###Tratamento de registros discrepantes que podem prejudicar a análise"""

dados_breve = dados_breve.query('(QUANTIDADE_TRAMITACOES > 1) & (TEMPO_TOTAL > 0)')

"""####Variável tempo total"""

dados_breve['TEMPO_TOTAL'].describe()

Q1 = dados_breve['TEMPO_TOTAL'].quantile(.25)
Q3 = dados_breve['TEMPO_TOTAL'].quantile(.75)
IIQ = Q3-Q1
limite_inferior = Q1 - (1.5 * IIQ)
limite_superior = Q3 + (1.5 * IIQ)

selecao = (dados_breve['TEMPO_TOTAL'] >= limite_inferior) & (dados_breve['TEMPO_TOTAL'] <= limite_superior)

df = dados_breve[selecao]
df['TEMPO_TOTAL'].describe()

dfa = df.groupby(['NOME_PROCESSO_PAE'])['TEMPO_TOTAL'].agg(['mean', 'min', 'max']).round(3)

dfa.columns = pd.MultiIndex.from_tuples((('BREVE_TEMPO_TOTAL', 'Média'), ('BREVE_TEMPO_TOTAL', 'Min'), ('BREVE_TEMPO_TOTAL', 'Max')))

dados_breve_agrupado = dfa

dados_breve_agrupado

"""####Variável Quantidade de Tramitações"""

dados_breve['QUANTIDADE_TRAMITACOES'].describe()

Q1 = dados_breve['QUANTIDADE_TRAMITACOES'].quantile(.25)
Q3 = dados_breve['QUANTIDADE_TRAMITACOES'].quantile(.75)
IIQ = Q3-Q1
limite_inferior = Q1 - (1.5 * IIQ)
limite_superior = Q3 + (1.5 * IIQ)

selecao = (dados_breve['QUANTIDADE_TRAMITACOES'] >= limite_inferior) & (dados_breve['QUANTIDADE_TRAMITACOES'] <= limite_superior)

df = dados_breve[selecao]
df['QUANTIDADE_TRAMITACOES'].describe()

dfa = df.groupby(['NOME_PROCESSO_PAE'])['QUANTIDADE_TRAMITACOES'].agg(['mean', 'min', 'max']).round(3)

dfa.columns = pd.MultiIndex.from_tuples((('BREVE_QUANTIDADE_TRAMITACOES', 'Média'), ('BREVE_QUANTIDADE_TRAMITACOES', 'Min'), ('BREVE_QUANTIDADE_TRAMITACOES', 'Max')))

dados_breve_agrupado = dados_breve_agrupado.join(dfa)
dados_breve_agrupado

"""####Variável Tempo Médio entre Tramitações"""

dados_breve['TEMPO_MEDIO_TRAMITACAO'].describe()

Q1 = dados_breve['TEMPO_MEDIO_TRAMITACAO'].quantile(.25)
Q3 = dados_breve['TEMPO_MEDIO_TRAMITACAO'].quantile(.75)
IIQ = Q3-Q1
limite_inferior = Q1 - (1.5 * IIQ)
limite_superior = Q3 + (1.5 * IIQ)

selecao = (dados_breve['TEMPO_MEDIO_TRAMITACAO'] >= limite_inferior) & (dados_breve['TEMPO_MEDIO_TRAMITACAO'] <= limite_superior)

df = dados_breve[selecao]
df['TEMPO_MEDIO_TRAMITACAO'].describe()

dfa = df.groupby(['NOME_PROCESSO_PAE'])['TEMPO_MEDIO_TRAMITACAO'].agg(['mean', 'min', 'max']).round(3)

dfa.columns = pd.MultiIndex.from_tuples((('BREVE_TEMPO_MEDIO_TRAMITACAO', 'Média'), ('BREVE_TEMPO_MEDIO_TRAMITACAO', 'Min'), ('BREVE_TEMPO_MEDIO_TRAMITACAO', 'Max')))

dados_breve_agrupado = dados_breve_agrupado.join(dfa)
dados_breve_agrupado

"""##Carga e Preparação dos dados do PAE"""

dados_pae = pd.read_excel('/content/drive/MyDrive/Colab Notebooks/Dados/DS - Processo ADM/dados.pae.xlsx')
dados_pae.describe()

"""###Tratamento de registros discrepantes que podem prejudicar a análise

####Variável tempo total
"""

dados_pae['TEMPO_TOTAL'].describe()

Q1 = dados_pae['TEMPO_TOTAL'].quantile(.25)
Q3 = dados_pae['TEMPO_TOTAL'].quantile(.75)
IIQ = Q3-Q1
limite_inferior = Q1 - (1.5 * IIQ)
limite_superior = Q3 + (1.5 * IIQ)

selecao = (dados_pae['TEMPO_TOTAL'] >= limite_inferior) & (dados_pae['TEMPO_TOTAL'] <= limite_superior)

df = dados_pae[selecao]
df['TEMPO_TOTAL'].describe()

dfa = df.groupby(['NOME_PROCESSO'])['TEMPO_TOTAL'].agg(['mean', 'min', 'max']).round(3)

dfa.columns = pd.MultiIndex.from_tuples((('PAE_TEMPO_TOTAL', 'Média'), ('PAE_TEMPO_TOTAL', 'Min'), ('PAE_TEMPO_TOTAL', 'Max')))

dados_pae_agrupado = dfa

dados_pae_agrupado

"""####Variável Quantidade de Tramitações"""

dados_pae['QUANTIDADE_TRAMITACOES'].describe()

Q1 = dados_pae['QUANTIDADE_TRAMITACOES'].quantile(.25)
Q3 = dados_pae['QUANTIDADE_TRAMITACOES'].quantile(.75)
IIQ = Q3-Q1
limite_inferior = Q1 - (1.5 * IIQ)
limite_superior = Q3 + (1.5 * IIQ)

selecao = (dados_pae['QUANTIDADE_TRAMITACOES'] >= limite_inferior) & (dados_pae['QUANTIDADE_TRAMITACOES'] <= limite_superior)

df = dados_pae[selecao]
df['QUANTIDADE_TRAMITACOES'].describe()

dfa = df.groupby(['NOME_PROCESSO'])['QUANTIDADE_TRAMITACOES'].agg(['mean', 'min', 'max']).round(3)

dfa.columns = pd.MultiIndex.from_tuples((('PAE_QUANTIDADE_TRAMITACOES', 'Média'), ('PAE_QUANTIDADE_TRAMITACOES', 'Min'), ('PAE_QUANTIDADE_TRAMITACOES', 'Max')))

dados_pae_agrupado = dados_pae_agrupado.join(dfa)
dados_pae_agrupado

"""####Variável Tempo Médio entre Tramitações"""

dados_pae['TEMPO_MEDIO_TRAMITACAO'].describe()

Q1 = dados_pae['TEMPO_MEDIO_TRAMITACAO'].quantile(.25)
Q3 = dados_pae['TEMPO_MEDIO_TRAMITACAO'].quantile(.75)
IIQ = Q3-Q1
limite_inferior = Q1 - (1.5 * IIQ)
limite_superior = Q3 + (1.5 * IIQ)

selecao = (dados_pae['TEMPO_MEDIO_TRAMITACAO'] >= limite_inferior) & (dados_pae['TEMPO_MEDIO_TRAMITACAO'] <= limite_superior)

df = dados_pae[selecao]
df['TEMPO_MEDIO_TRAMITACAO'].describe()

dfa = df.groupby(['NOME_PROCESSO'])['TEMPO_MEDIO_TRAMITACAO'].agg(['mean', 'min', 'max']).round(3)

dfa.columns = pd.MultiIndex.from_tuples((('PAE_TEMPO_MEDIO_TRAMITACAO', 'Média'), ('PAE_TEMPO_MEDIO_TRAMITACAO', 'Min'), ('PAE_TEMPO_MEDIO_TRAMITACAO', 'Max')))

dfa

dados_pae_agrupado = dados_pae_agrupado.join(dfa)
dados_pae_agrupado

"""##Consolidação dos Dados para Comparação"""

dados_consolidados = dados_pae_agrupado.join(dados_breve_agrupado)
dados_consolidados

dados_consolidados.to_excel('dados.consolidados.xls')

dados_consolidados_media = dados_consolidados[pd.MultiIndex.from_tuples(( ('PAE_TEMPO_TOTAL', 'Média'), ('BREVE_TEMPO_TOTAL', 'Média'), 
                                                   ('PAE_QUANTIDADE_TRAMITACOES', 'Média'), ('BREVE_QUANTIDADE_TRAMITACOES', 'Média'),
                                                   ('PAE_TEMPO_MEDIO_TRAMITACAO', 'Média'), ('BREVE_TEMPO_MEDIO_TRAMITACAO', 'Média') ))]

dados_consolidados_media.columns = pd.MultiIndex.from_tuples((('TEMPO_TOTAL', 'Média PAE'), ('TEMPO_TOTAL', 'Média Breve'),  
                                       ('QUANTIDADE_TRAMITACOES', 'Média PAE'), ('QUANTIDADE_TRAMITACOES', 'Média Breve'),
                                       ('TEMPO_MEDIO_TRAMITACAO', 'Média PAE'), ('TEMPO_MEDIO_TRAMITACAO', 'Média Breve')
                                       ))

dados_consolidados_media

dados_consolidados_media.to_excel('dados.consolidados.media.xls')

#converte as colunas com indexação multipla para o padrão 
dados_comp_grafico = dados_consolidados_media.copy()
dados_comp_grafico.columns = ['_'.join(col) for col in dados_comp_grafico.columns.values]

dados_comp_grafico.reset_index(inplace=True)
dados_comp_grafico.head()

"""##Análise do Estudo Realizado

Ficou evidente na análise um importante ganho de desempenho ao se empregar um engine de workflow (automação de processos) em consideração ao modelo anterior que grande parte das atividades eram feitas manualmente.

A integração entre os sistemas legados, otimização dos processos resultou em um ganho médio de **60%** de redução do tempo total para execução de processos administrativos de mesma natureza.
"""