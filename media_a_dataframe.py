from cmath import nan
import pandas as pd
import numpy as np

velas = pd.read_csv("", sep="\t")
velas = velas.copy()

medias = {}
for i in range(2, 5):
    medias[f"{i}"] = velas["<CLOSE>"].rolling(i).mean()
    


resultados = pd.DataFrame(medias)

a = pd.concat((velas, resultados),axis=1)
a.to_csv('totales.csv', header=True, index=False)
