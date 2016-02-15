#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 18:53:10 2016

@author: helio
"""
import sys
import numpy as np

mensagem = '\nCalculo do fator de expansao atraves de Progressao Geometrica\n'
mensagem += 'Uso:\nFator de expansao'
mensagem += ' / Comprimento total / Tam do primeiro volume.\n'
print(mensagem)


try:
    q = float(sys.argv[1])
except:
    q = input('Digite o fator de expansao [1.1 ou 1.2]: ')

try:
    X = float(sys.argv[2])
except:
    X = input('\nDigite o comprimento total: ')
    
try:
    a1 = float(sys.argv[3])
except:
    a1 = input('\nDigite o tamanho do primeiro volume: ')
    
n = int(np.ceil(np.log(((X/a1)*(q-1))+1)/np.log(q)))

outN = '\nNumero de volumes para fator de expansao ' + str(q) + ' = ' + str(n)
outN += ' Volumes'
print (outN)

an = a1*q**(n-1)

fe = an/a1

print ('Fator de expansao para o OpenFOAM = ' + str(fe))