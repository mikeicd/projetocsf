import os
import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

basedir = os.path.abspath(os.path.dirname(__file__))

files = os.listdir(f'{basedir}/data')

df_list = []
for file in files:
    print(file)
    df = pd.read_csv("data/"+file)
    df = df.groupby('Date and Time').first()

    df_list.append(df)
    print(df.head())

for df in df_list:
    print(df['rssi'].mean())
    

locais = {}

# for item in files:
#     locais[item[:-4]] = {}
#     print(item)
#     with open(f'{basedir}/data/{item}', encoding="utf8") as csv_file:
#         csv_data = csv.reader(csv_file, delimiter=',')
#         lista = []
#         first_line = True
#         for row in csv_data:
#             if not first_line:
#                 lista.append(float(row[1]))

#             first_line = False
#         locais[item[:-4]]['rssi'] = lista

# for key, value in locais.items():
#     print(key)
#     value['max'] = np.max(value['medidas'])
#     value['min'] = np.min(value['medidas'])
#     value['mean'] = np.mean(value['medidas'])
