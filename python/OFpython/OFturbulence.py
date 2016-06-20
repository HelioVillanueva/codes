#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Fri May 20 10:54:42 2016

@author: helio
"""

import sys
import numpy as np

msg1 = '\nCalcula condicoes de contorno para modelos de turbulencia (k,e,w)'
msg2 = '\nModo de uso (argumentos):\n1-Velocidade media entrada'
msg2 += '\n2-Intensidade turbulenta\n3-Comprimento caracteristico'

try:
    if sys.argv[1] == '-h':
        print msg1+msg2
        
except:
    pass

try:
    U = float(sys.argv[1])
except:
    U = input('Digite o valor da Velocidade media na entrada [m/s]: ')
    
try:
    I = float(sys.argv[2])
except:
    I = input('Digite o valor da intensidade turbulenta [%]: ')
try:
    dh = float(sys.argv[3])
except:
    dh = input('Digite o valor do diametro hidraulico [m]: ')

k = (3./2 * (U*I)**2)
print('\nO valor de k é: ' +str(k) +'\n')

l = 0.038*dh
e = (0.09) * (k**1.5)/l
print('O valor de epsilon é: ' +str(e))

w = np.sqrt(k)/l
print('\nO valor de omega é: ' +str(w))

## -- Reynolds global
nu = 1.5e-5 # m2/s -> para o ar

Re = U * l/nu

print('\nNumero de Reynolds para ar: ' +str(Re) + '\n')