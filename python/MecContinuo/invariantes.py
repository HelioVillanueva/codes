#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def calc(tensor):
    '''
    Calcula os invariantes do tensor passado como argumento
    resultando [I1 I2 I3]
    '''
    I1 = np.trace(tensor) # 1 invariante
    I2 = 0.5*((I1**2)- np.trace(np.dot(tensor,tensor))) # 2 invariante
    I3 = np.linalg.det(tensor) # 3 invariante
    
    return np.array([I1,I2,I3])