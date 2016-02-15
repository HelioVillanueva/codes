# -*- coding: utf-8 -*-
import numpy as np

def out(tensor,coord,invariantes,eigval,eigvet,D,W,plano,t,Tn,tal):
    '''
    Imprimi na tela o resultados dos calculos de forma
    organizada
    '''
    print('\n===============\nTensor entrada T:\n')
    print tensor
    print('\n===============\nEm coordenadas ' + coord + ',')
    print ('os invariantes do tensor T sao:\n')
    print invariantes
    print('\n===============\nOs autovalores estão na matriz abaixo:\n')
    print eigval*np.identity(3)
    print('\nOs autovetores (dispostos em colunas) na matriz abaixo:\n')
    print eigvet
    print('\n===============\nParte simetrica (D) do tensor T:\n')
    print D
    print('\nParte antisimetrica (W) do tensor T:\n')
    print W
    print('\nVetor tensao no dado plano ' + str(plano) + ':\n')
    print t
    print('\nTensao normal no plano:\n')
    print Tn
    print('\nTensao cisalhante no plano:\n')
    print tal
    return 0