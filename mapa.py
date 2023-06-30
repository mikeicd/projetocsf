import folium
from folium.plugins import HeatMap
import pandas as pd


def cria_mapa(df:pd.DataFrame):

    # Criar um mapa com base em uma localização inicial
    mapa = folium.Map(location=[-27.608355, -48.633345], zoom_start=15)

    # Lista de coordenadas de latitude e longitude
    coordenadas = []

    # Extrair coordenadas do JSON
    i = 0
    for indice, dado in df.iterrows():
        lat = dado['Lat']
        lon = dado['Long']
        pot = dado['RSSI']
        coordenadas.append([lat, lon, pot])
        i += 1

    # Criação do objeto HeatMap com as coordenadas
    heatmap = HeatMap(coordenadas)
    # Adicionar o mapa de calor ao mapa
    heatmap.add_to(mapa)

    # Salvar o mapa em um arquivo HTML
    mapa.save('mapa_de_calor.html')
