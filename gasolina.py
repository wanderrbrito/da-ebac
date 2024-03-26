# Importando as bibliotecas
import csv
import pandas as pd
import matplotlib.pylab as plt

# Lendo arquivo CSV e criando Dataframe
preco_gasolina_df = pd.read_csv('gasolina.csv')
preco_gasolina_df

# Gerando grafico de linhas e salvado o grafico como .png
preco_gasolina_df.plot('dia',"venda")
plt.savefig('gasolina.png')
