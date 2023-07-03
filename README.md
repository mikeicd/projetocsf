## Medições

Nas tabelas a seguir são apreentados os valores de latitude e longitude dos pontos de medições.
### Coordenadas dos pontos *indoor*

|        local        | distância (m) |   latitude  |  longitude  |
|:-------------------:|:-------------:|:-----------:|:-----------:|
| gateway             |         -     | -27.60795022| -48.63369853|
| Indor-porta-aberta  |         59,71 | -27.608177  | -48.633219  |
| Indor-porta-fechada |         59,71 | -27.6081634 | -48.6338594 |
| auditorio           |         52,29 | -27.608355  | -48.633345  |
| labic-1             |         54,67 | -27.608155  | -48.633180  |
| acesso-quadra       |         57,93 | -27.608341  | -48.633.263 |
| mesa                |          63,5 | -27.608439  | -48.633288  |
| biblioteca          |          82,9 | -27.608604  | -48.633205  |
| labic-2             |         48,35 | -27.6082194 | -48.6333502 |
| frente-ifsc         |        131,77 | -27.608117  | -48.632395  |
| lab-com             |         54,89 | -27.608245  | -48.633300  |

### Coordenadas dos pontos *outdoor*

|        local        | distância (m) |   latitude  |  longitude  |
|:-------------------:|:-------------:|:-----------:|:-----------:|
| frente-bistek       |       1014,65 | -27.606824  | -48.623519  |
| multiuso            |       2285,27 | -27.603.642 | -48.610991  |
| laje-1              |         84,11 | -27.608464  | -48.633043  |
| portaria-frente     |        138,17 | -27.6081508 | -48.6323943 |
| inicio-beira-mar    |          1999 | -27.6039654 | -48.6141063 |
| fim-beira-mar       |          3015 | -27.6026611 | -48.6023764 |
| abraao-beira-mar    |          3580 | -27.611220  | -48.597652  |
| posto-perto-ifsc    |        407,45 | -27.604444  | -48.632901  |
| mundo-car           |          1970 | -27.5958768 | -48.6191918 |
## Simulação dos pontos *outdoor* no *Radio Mobile*

Os pontos das medições *outdoor* foram utilizados para simulação com o *software* *Radio Mobile* e os resultados estão em arquivos html no diretório [radio-mobile](./radio-mobile/).

## Comparação entre dados medidos e simulados

A tabela a seguir apresenta uma comparação dos valores de Potência Recebida (RSSI) e Perda de caminho (PL) entre o dados medidos e simulados, considerando somente os pontos *outdoor*.

|       Local    |RSSI medido (dBm)|PL medido (dB)   |RSSI simulado (dBm)|PL simulado (dB)|
|----------------|-------------|----------|-------------|-------|
|laje-1          |-82,43  |96,32 |-61,59       |75,48  |
|abrao-beira-mar |-102,60 |116,49|-101,96      |115,85 |
|posto-perto-ifsc|-77,80  |91,69 |-76,91       |90,80  |
|fim-beira-mar   |-108,05 |121,94|-91,91       |105,80 |
|frente-ifsc     |-90,46  |104,34|-62,16       |76,05  |
|frente-bistek   |-96,80  |110,69|-79,38       |93,27  |
|multiuso        |-100,42 |114,31|-88,14       |102,03 |
|mundo-car       |-109,83 |123,72|-87,18       |101,07 |
|inicio-beira-mar|-98,87  |112,76|-85,98       |99,87  |
## Determinar o expoente de perda (n)
N = 2.87

### Definir 'd0' e 'P0'
d0 = 8.75
P0 = 98.18

## Mapa de 'calor' 


## Conclusões