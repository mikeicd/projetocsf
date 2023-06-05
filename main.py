import os, csv

basedir = os.path.abspath(os.path.dirname(__file__))

files = os.listdir(f'{basedir}/data')

locais={}

for item in files:
    locais[item[:-4]] = {}
    print(item)
    with open(f'{basedir}/data/{item}', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        lista = []    
        for row in csv_data:
            lista.append(row[1])
        locais[item[:-4]]['medidas'] = lista
                
print(locais)
            
