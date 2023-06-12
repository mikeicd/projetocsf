import os, csv, pprint
import numpy as np
import matplotlib.pyplot as plt

basedir = os.path.abspath(os.path.dirname(__file__))

files = os.listdir(f'{basedir}/data')

locais={}

for item in files:
    locais[item[:-4]] = {}
    print(item)
    with open(f'{basedir}/data/{item}', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        lista = []
        first_line = True 
        for row in csv_data:
            if not first_line:
                lista.append(float(row[1]))
            first_line = False
        locais[item[:-4]]['medidas'] = lista
                
for key, value in locais.items():
    print(key)
    value['max'] = np.max(value['medidas'])
    value['min'] = np.min(value['medidas'])
    value['mean'] = np.mean(value['medidas'])

base_x = 50
base_y = 10
locais['acesso-quadra']['coord'] = (base_x + 0, base_y + 42)
locais['labic']['coord'] = (base_x - 13, base_y + 42)
locais['auditorio']['coord'] = (base_x + 0, base_y + 52)
locais['mesa']['coord'] = (base_x + 2, base_y + 69)
locais['biblioteca']['coord'] = (base_x + 0, base_y + 80)


# pprint.pprint(locais)

# Define grid parameters
grid_size = 100
x = np.linspace(0, grid_size, grid_size)
y = np.linspace(0, grid_size, grid_size)
X, Y = np.meshgrid(x, y)

# Interpolate signal strength measurements to grid points
Z = np.zeros((grid_size, grid_size))
for local in locais:
    x, y = locais[local]['coord']
    Z[y, x] = locais[local]['mean']
    
# Generate heatmap
plt.imshow(Z, cmap='hot', interpolation='nearest', origin='lower')
plt.colorbar()
plt.scatter(base_x,base_y, color='black', label='Gateway')
plt.show()
        
            
