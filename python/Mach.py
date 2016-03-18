#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 10:02:37 2016

@author: helio
"""

def simple(vel,c=343.2):
    '''
        Calcula o numero de Mach como Ma = vel/c
        
        vel - velocidade (m/s)
        c   - velocidade do som. Para ar 20C = 343.2 (padrao)
    '''
    Ma = vel/c
    if Ma<1.0:
        print('Escoamento subsonico')
    elif Ma>1.0:
        print('Escoamento supersonico')
    else:
        print('Escoamento transonico')
    return Ma