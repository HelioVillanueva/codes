#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def calc(tensor,plano):
    '''
    Calcula o vetor tensao em um dado plano assim como a tensao normal e
    cisalhante nesse plano
    Retorna t --> vetor tensao
            Tn --> tensao normal
            tal --> tensao cisalhante
    '''
    n = plano/np.linalg.norm(plano)
    t = np.dot(tensor,n)
    Tn = np.dot(n,t)
    tal = np.sqrt( np.square(np.linalg.norm(t)) - np.square(Tn))
    return t, Tn, tal