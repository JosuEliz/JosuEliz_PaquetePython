from PaqueteJosuEliz import norm_estand_class as normstand
import numpy as np

def test_all():
    """Executes the tests to verify the installation has ben successfull"""
    data1=(11.5, 1.2, 0.5, 5.3, 20.5, 8.4)
    datos_tratados=normstand.Norm_stand(data1)
    print(datos_tratados.normalizado)
    print(datos_tratados.estandarizado)
    datos_tratados.printResults()

test_all()  