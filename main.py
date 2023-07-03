import os
import pandas as pd
from calculo_perda import perda_caminho
from mapa import cria_mapa

basedir = os.path.abspath(os.path.dirname(__file__))
PotTx = 13.89


def coleta_dados(path):
    files = os.listdir(f'{basedir}/{path}')

    df_list = []
    for file in files:
        if file.endswith('.csv'):
            df = pd.read_csv(f'{basedir}/{path}/{file}')
            df = df.groupby('Date and Time').first()
            df['Nome'] = file[:-4]
            df_list.append(df)

    df_coord = pd.read_json("./data/coordenadas.json")

    df_total = pd.DataFrame(columns=['Nome', 'RSSI', 'Distc', 'Lat', 'Long'])

    for df in df_list:
        df_teste = pd.DataFrame()
        df_teste['Distc'] = df_coord['distancia'].loc[df_coord['local']
                                                      == df['Nome'][0]]
        df_teste['Lat'] = df_coord['latitude'].loc[df_coord['local']
                                                   == df['Nome'][0]]
        df_teste['Long'] = df_coord['longitude'].loc[df_coord['local']
                                                     == df['Nome'][0]]
        df_teste['Nome'] = df['Nome'][0]
        df_teste['RSSI'] = df['rssi'].mean()
        df_teste['Pl'] = PotTx - df['rssi'].mean()
        df_total = pd.concat([df_total, df_teste])

    df_total.reset_index(inplace=True, drop=True)
    print(df_total.head(100))
    return df_total


def processa_dados(df):
    id = df['Distc'].idxmin()
    rssi = df.loc[id, 'RSSI']
    dist = df.loc[id, 'Distc']
    nome = df.loc[id, 'Nome']
    print(f'{nome}')
    parametro = perda_caminho(distancias=df['Distc'].to_list(
    ), perdas=df['RSSI'].to_list(), d0=dist, pl_d0=rssi)
    return parametro


df_indoor = coleta_dados('data/indoor')
df_outdoor = coleta_dados('data/outdoor')

parametro_indoor = processa_dados(df_indoor)
parametro_outdoor = processa_dados(df_outdoor)

print(parametro_indoor)
print(parametro_outdoor)

cria_mapa(
    df=df_indoor,
    nome_mapa='mapa_indoor',
    zoom=100,
    radius=10,
    centro=[-27.608355, -48.633345])

cria_mapa(
    df=df_outdoor,
    nome_mapa='mapa_outdoor',
    zoom=15,
    radius=30,
    centro=[-27.606824, -48.623519])
