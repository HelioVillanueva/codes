#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt
# -- Vetor gravidade
g = np.array([0,-9.81,0])

# -- Vetor posicao inicial
x0 = np.array([0,0,0])

# -- Vetor velocidade inicial
v0 = np.array([0.01,0.1,0.1])

# -- num pontos calculados no tempo
nPoints = 100

## ========================================================================= ##
# -- Determina t final quando y é 0
coeff = [g[1]/2,v0[1],0]
raizes = np.roots(coeff)
t = raizes[0]
# -- Inicializa campo do espaco em func tempo e passo de tempo
dt = np.linspace(0.0, t, num=nPoints)
x = np.zeros((nPoints,3))
# -- Calcula a posicao no espaco para cada passo de tempo
for i,ti in enumerate(dt):
    x[i] = x0 + g*(ti**2)/2 + v0*ti

plt.plot(x[:,0],x[:,1])

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x[:,0], x[:,2], x[:,1], label='parametric curve')
ax.legend()

plt.show()

