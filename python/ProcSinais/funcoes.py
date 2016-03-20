#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def fTriang(ini,end,points,impr):
    '''Gera funcao triangulo
        ini - comeco da funcao
        end - final
        points - numero de pontos
        impr - plota grafico da funcao com o arg 'y'
    '''
    t = np.linspace(ini,end,points)
    e = np.zeros(len(t))
    
    for i in range(len(t)):
        e[i] = t[-1] - abs(t[i])
            
    if impr == 'y':
        plt.figure()        
        plt.plot(t,e,'-*')
        plt.grid(which='major', axis='both')
        plt.xlabel('t - time')
        plt.ylabel('e')
    
    return e
    
def fJanela(ini,end,points,inijan,endjan,intjan,impr):
    '''Gera funcao janela/retangular
        ini - comeco da funcao
        end - final
        points - numero de pontos
        inijan - inicio da janela
        endjan - final da janela
        intjan - intensidade
        impr - plota grafico da funcao com o arg 'y'
    '''
    t = np.linspace(ini,end,points)
    e = np.zeros(len(t))
    
    for i, ti in enumerate(t):
        if inijan<=ti<=endjan:
            e[i] = intjan
            
    if impr == 'y':
        plt.figure()        
        plt.plot(t,e,'-*')
        plt.grid(which='major', axis='both')
        plt.xlabel('t - time')
        plt.ylabel('e')
        
    return e

def fPenteDirac(ini,end,points,pts,impr):
    '''Gera funcao pente de Dirac
        ini - comeco da funcao
        end - final
        points - numero de pontos
        pts - lista com pontos onde pente e 1
        impr - plota grafico da funcao com o arg 'y'
    '''
    t = np.linspace(ini,end,points)
    e = np.zeros(len(t))
    
    e[pts] = 1    
    
    if impr == 'y':
        plt.figure()        
        plt.plot(t,e,'-*')
        plt.grid(which='major', axis='both')
        plt.xlabel('t - time')
        plt.ylabel('e')

    return e