import numpy as np

def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:

    try:
        return np.array(a) @ np.array(b)
    except ValueError:
        return -1
