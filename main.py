import os
import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from calculo_perda import perda_caminho
from mapa import cria_mapa

basedir = os.path.abspath(os.path.dirname(__file__))

files = os.listdir(f'{basedir}/data')

PotTx = 13.89

df_list = []
for file in files:
    if file.endswith('.csv'):
        df = pd.read_csv("data/"+file)
        df = df.groupby('Date and Time').first()
        df['Nome'] = file[:-4]

        df_list.append(df)

df_coord = pd.read_json("./data/coordenadas.json")

df_total = pd.DataFrame(columns=['Nome','RSSI','Distc','Lat','Long'])

for df in df_list: 
    df_teste = pd.DataFrame()    
    df_teste['Distc'] = df_coord['distancia'].loc[df_coord['local'] == df['Nome'][0]]
    df_teste['Lat'] = df_coord['latitude'].loc[df_coord['local'] == df['Nome'][0]]
    df_teste['Long'] = df_coord['longitude'].loc[df_coord['local'] == df['Nome'][0]]
    df_teste['Nome'] = df['Nome'][0]
    df_teste['RSSI'] = df['rssi'].mean()
    df_teste['Pl'] = PotTx - df['rssi'].mean()

    df_total = pd.concat([df_total, df_teste])

df_total.reset_index(inplace=True,drop=True)
print(df_total.head(100))

parametro = perda_caminho(distancias=df_total['Distc'].to_list(),perdas=df_total['Pl'].to_list(), d0=15, pl_d0=(PotTx -(-50)))



print(parametro)

cria_mapa(df_total)
