import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple


def plot_discrete_simple(
            n_range: np.ndarray, 
            x: np.ndarray, 
            figsize: Tuple = (4,2)
    ) -> plt.Axes:
    """
    Función simplificada para graficar una señal en tiempo discreto.
    
    Parámetros:
        - n_range (numpy.ndarray): Soporte discreto sobre el cual está definida la señal.
        - x (numpy.ndarray): Valor de la señal en cada instante.
        - figsize (tuple): Tamaño del plot.
    """
    
    fig, ax = plt.subplots(1,1,figsize=figsize)
    ax.stem(n_range,x,use_line_collection=True)
    ax.grid(True)
    ax.set_xlabel("n")
    ax.set_ylabel("x[n]")
    fig.tight_layout()
    return ax