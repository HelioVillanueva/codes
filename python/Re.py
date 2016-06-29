#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 09:15:05 2016

@author: helio
"""

def Re(vel,l,nu):
    '''Calcula o numero de Reynolds como:
    
        vel*X/nu
        
    vel - velocidade (m/s)
    
    X   - comprimento característico (m)

    nu = mu/rho - viscosidade cinemática (m2/s)

    mu  - viscosidade dinámica (Pa·s or N·s/m2 or kg/(m·s))
    
    rho - densidade (kg/m3)
    
    '''
    Re = vel*l/nu
    if Re<10.0:
        print('Escoamento laminar')
    elif Re>10000.0:
        print('Escoamento turbulento')
    else:
        print('Transicao laminar-turbulento')
    return Re
