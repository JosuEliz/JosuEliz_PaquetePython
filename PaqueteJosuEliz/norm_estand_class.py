import numpy as np
class Norm_stand:
    def __init__(self, x):
        norm = []
        rango=max(x)-min(x)
        estand = []
        media=np.mean(x)
        sde=np.std(x, ddof=1)
        for elemento in x:
            norm=np.append(norm,(elemento-min(x))/rango)
        self.normalizado=norm
        for elemento in x:
            estand=np.append(estand,(elemento-media)/sde)
        self.estandarizado=estand
    
    def printResults(self):
        print("Los datos normalizados: ",self.normalizado,"\nLos datos estandarizados: ",self.estandarizado)