# Arquivo de testes
import numpy as np
import RobPy as rp

v1 = rp.cria_vetor3([1,0,0])
v2 = rp.cria_vetor3([0,1,0])

print(rp.ang_vetores(v2,v1) * 180 / np.pi)