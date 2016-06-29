#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 10:02:37 2016

@author: helio
"""
import numpy as np

def simple(vel,Rspc = 287.058,T = 20 + 273,gamma = 1.4):
    '''
        Calcula o numero de Mach como Ma = vel/c
        
        vel - velocidade (m/s)
        
        c   - velocidade do som = np.sqrt(gamma*Rspc*T)
        
        gamma - razao calor específicos cp/cv
        
        Rspc - constante dos gases específica
        
        T - temperatura [K]
    '''
    
    c = np.sqrt(gamma*Rspc*T)
    
    Ma = vel/c
    print Ma

    if Ma<1.0:
        print('Escoamento subsonico')
    elif Ma>1.01:
        print('Escoamento supersonico')
    else:
        print('Escoamento transonico')
    return Ma
    
# Ex
#ma = simple(343.14894,gamma=1.387,T=400+273)