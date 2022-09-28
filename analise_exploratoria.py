# -*- coding: utf-8 -*-
"""Analise Exploratoria.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fbtd55GHCoeco4vBPRBYgFbKGlVsV3UH
"""

#Importando as bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn")

#Upload do arquivo
from google.colab import files
arq = files.upload()

#Criando nosso DataFrame
df = pd.read_excel("/content/drive/My Drive/Colab/datasets/AdventureWorks.xlsx")

#Visualizando as 5 primeiras linhas
df.head()

#Quantidade de linhas e colunas
df.shape

#verificando os tipos de dados
df.dtypes

#Qual a receita total?
df["Valor Venda"].sum()

#Qual o custo total?
df["custo"] = df["Custo Unitário"].mul(df["Quantidade"])#Criando a coluna de custo

df.head(1)

#Qual o custo total?
round(df["custo"].sum(),2)

#Agora que temos a receita e custo e o total, podemos achar o lucro total
#Vamos criar uma coluna de lucro que será receita - custo
df["lucro"] = df["Valor Venda"] - df["custo"]

df.head(1)

#Total lucro
round(df["lucro"].sum(),2)

#Criando uma coluna com total de dias para enviar o produto
df["Tempo_envio"] = df["Data Envio"] - df["Data Venda"]

df.head(1)

df.head(1)

"""Agora, queremos saber a média do tempo de envio para cada marca, e para isso precisamos transformar a coluna tempo_envio em numerico"""

#Extraindo apenas os dias
df["Tempo_envio"] = (df["Data Envio"] - df["Data Venda"]).dt.days

df.head(1)

#Verificando o tipo da coluna tempo_envio
df["Tempo_envio"].dtype

#Média do tempo de envio por marca
df.groupby("Marca")["Tempo_envio"].mean()

"""Missing Values"""

#Verificando se temos dados faltantes
df.isnull().sum()

"""e, se a gente quiser saber o lucro por ano e por marca"""

#Vamos agrupar por ano e marca
df.groupby([df["Data Venda"].dt.year, "Marca"])["lucro"].sum()

pd.options.display.float_format = '{:20,.2f}'.format

#Resetando o index
lucro_ano = df.groupby([df["Data Venda"].dt.year, "Marca"])["lucro"].sum().reset_index()
lucro_ano

#Gráfico total de produtos vendidos
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False)

#Gráfico total de produtos vendidos
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False).plot.barh(title="Total produtos vendidos")
plt.xlabel("Total")
plt.ylabel("Produto");

df.groupby(df["Data Venda"].dt.year)["lucro"].sum().plot.bar(title="Lucro x Ano")
plt.xlabel("Ano")
plt.ylabel("Receita");

df.groupby(df["Data Venda"].dt.year)["lucro"].sum()

df_2009 = df[df["Data Venda"].dt.year == 2009]

df_2009.head()

df_2009.groupby(df_2009["Data Venda"].dt.month)["lucro"].sum().plot(title="Lucro x Ano")
plt.xlabel("Ano")
plt.ylabel("lucro");

df_2009.groupby("Marca")["lucro"].sum().plot.bar(title="Lucro x Marca")
plt.xlabel("Marca")
plt.ylabel("lucro")
plt.xticks(rotation="horizontal");

df_2009.groupby("Classe")["lucro"].sum().plot.bar(title="Lucro x Classe")
plt.xlabel("Classe")
plt.ylabel("lucro")
plt.xticks(rotation="horizontal");

df["Tempo"]