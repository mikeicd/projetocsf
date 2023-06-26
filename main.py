import os
import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from calculo_perda import perda_caminho

basedir = os.path.abspath(os.path.dirname(__file__))

files = os.listdir(f'{basedir}/data')

PotTx = 14

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
    df_teste['Distc'] = df_coord['distância'].loc[df_coord['local'] == df['Nome'][0]]
    df_teste['Lat'] = df_coord['latitude'].loc[df_coord['local'] == df['Nome'][0]]
    df_teste['Long'] = df_coord['longitude'].loc[df_coord['local'] == df['Nome'][0]]
    df_teste['Nome'] = df['Nome'][0]
    df_teste['RSSI'] = df['rssi'].mean()
    df_teste['Prx'] = PotTx + df['rssi'].mean() *-1

    df_total = pd.concat([df_total, df_teste])

df_total.reset_index(inplace=True,drop=True)
print(df_total.head(100))

parametro = perda_caminho(distancias=df_total['Distc'].to_list(),perdas=df_total['Prx'].to_list(), d0=10, pl_d0=(PotTx + -60.0)*-1)

print(parametro)


