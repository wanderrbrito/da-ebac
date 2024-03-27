# código de geração do gráfico 
# Importando as bibliotecas
import csv
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns

# Lendo arquivo CSV e criando Dataframe
preco_gasolina_df = pd.read_csv('gasolina.csv')
preco_gasolina_df = preco_gasolina_df.rename(columns={'venda':'preco'})
preco_gasolina_df

# Gerando grafico de linhas e salvado o grafico como .png
sns.lineplot(data=preco_gasolina_df, x='dia', y='preco', color='blue')
plt.title('Variacao do Preço da Gasolina por Dia')
plt.savefig('gasolina.png')
