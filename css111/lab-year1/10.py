import pandas as pd
import numpy as np


def FVIF(r, n, PV=1):
    cells = np.ones(shape=(n, r)) * PV

    for row in range(n):
        for col in range(r):
            cells[row, col] = PV * ((col + 1) / 100 + 1) ** (row + 1)

    cells = np.round(cells, 3)
    table = [{f"{idx}%": fv for idx, fv in enumerate(
        cells[i], 1)} for i in range(n)]
    df = pd.DataFrame(table)
    df.index.name = "Period"
    df.index += 1
    return df