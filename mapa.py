import folium
from folium.plugins import HeatMap
import json
import pandas as pd

# Ler o JSON
with open('data/coordenadas.json', 'r') as arquivo:
    dados = json.load(arquivo)

# Criar um mapa com base em uma localização inicial
mapa = folium.Map(location=[-27.608355, -48.633345], zoom_start=15)

# Lista de coordenadas de latitude e longitude
coordenadas = []

# Extrair coordenadas do JSON
i = 0
for dado in dados:
    lat = float(dado['latitude'])
    lon = float(dado['longitude'])
    #coordenadas.append([lat, lon, locais.get(i)]) TODO alterar aqui para incluir a intensidade
    coordenadas.append([lat, lon])
    i += 1

# Criação do objeto HeatMap com as coordenadas
heatmap = HeatMap(coordenadas)

# Adicionar o mapa de calor ao mapa
heatmap.add_to(mapa)

# Salvar o mapa em um arquivo HTML
mapa.save('mapa_de_calor.html')