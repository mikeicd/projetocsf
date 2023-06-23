import numpy as np
from scipy.optimize import curve_fit


def perda_caminho(distancias, perdas, d0, pl_d0, N):
    def modelo(distancias, N):
        return pl_d0 + 10 * N * np.log10(distancias/d0)

    p0 = N  # Valor inicial para o expoente N
    parametros, _ = curve_fit(modelo, distancias, perdas, p0=p0)

    return parametros[0]



dist = [40, 20, 30, 40, 50]
perd = []