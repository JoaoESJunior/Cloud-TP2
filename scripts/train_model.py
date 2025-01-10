
import os
import pandas as pd
from fpgrowth_py import fpgrowth

print("Carregando o dataset...")
dataset_path = "/home/joaojunior/project2-pv2/2023_spotify_ds1.csv"
output_model = "/home/joaojunior/project2-pv2/model.pickle"

df = pd.read_csv(dataset_path)
print("Processando o dataset...")

# Geração das regras de associação
transactions = df.groupby("pid")["track_name"].apply(list).tolist()
freq_itemsets, rules = fpgrowth(transactions, minSupRatio=0.01, minConf=0.5)

print("Treinando o modelo...")
pd.to_pickle(rules, output_model)
print(f"Modelo salvo em {output_model}")
