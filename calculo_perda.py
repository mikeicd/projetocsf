import numpy as np
from scipy.optimize import minimize


def perda_caminho(distancias, perdas, d0, pl_d0):
    def modelo(distancias, N):
        return pl_d0 + (10 * N * np.log10(np.divide(distancias,d0)))

    def loss_function(params):
        y_pred = modelo(distancias, *params)
        mse = np.sum((perdas - y_pred)**2)
        return mse   
    
    p0 = 2  # Valor inicial para o expoente N
    result = minimize(loss_function, p0, method='Nelder-Mead')    
    return result


