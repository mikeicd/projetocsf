import numpy as np
import pandas as pd
from scipy.optimize import curve_fit, minimize


def perda_caminho(distancias, perdas, d0, pl_d0):
    def modelo(distancias, N):
        return pl_d0 + (10 * N * np.log10(np.divide(distancias,d0)))

    def loss_function(params):
        y_pred = modelo(distancias, *params)
        mse = np.mean((perdas - y_pred)**2)
        return mse   
    
    p0 = 2  # Valor inicial para o expoente N
    # parametros, _, infodict, errmsg, ier = curve_fit(modelo, distancias, perdas, p0=p0,full_output=True)
    result = minimize(loss_function, p0, method='Nelder-Mead')

    
    return result



# df = pd.read_json("./data/coordenadas.json")
# print(df.head())

