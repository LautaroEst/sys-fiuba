import numpy as np


def discrete_delta(n_range: np.ndarray) -> np.ndarray:
    """
    Función vectorizada de la delta de dirac discreta.
    
    Parámetros:
        - n_range (numpy.ndarray): Rango de valores sobre el cual está definida la delta.
        Debe ser un numpy.ndarray con shape (N,)
    """

    if len(n_range.shape) != 1:
        raise ValueError("n_range tiene que ser un array unidimensional.")
    
    x = np.zeros(n_range.shape,dtype=float)
    x[n_range == 0] = 1.

    return x


def discrete_step(n_range: np.ndarray, u0: float = 1.) -> np.ndarray:
    """
    Función vectorizada del escalón unitario discreto.

    Parámetros:
        - n_range (numpy.ndarray): Rango de valores sobre el cual está definida la delta.
        Debe ser un numpy.ndarray con shape (N,).
        - u0 (float): Valor del escalón en n = 0.
    """

    if len(n_range.shape) != 1:
        raise ValueError("n_range tiene que ser un array unidimensional.")
    
    x = np.zeros(n_range.shape,dtype=float)
    x[n_range > 0 ] = 1.
    x[n_range == 0] = u0

    return x


