# -*- coding: utf-8 -*-

import numpy as np
import cantera as ct
import kanthalA1props as A1prop

class preHeat(object):
    '''Creates de heater object
    
    Units:
    
    n - N of passages [-]
    
    massFlow - [kg/s]
    
    T* - [C]
    
    cp - [J/kg K]

    Q - Total heat [W]
    
    q - heat each passage [W]
    
    U - [Volts]
    
    R - [Ohms]
    
    I - [A]
    
    h - [W/m2 K]
    
    Variables for each coil/passages
    
    L - coil stretched length [m]
    
    l - coil retracted length [m]
    
    p - coil pitch (default=0.01) [m]
    
    N - coil N of turns [-]
    
    Vres - coil volume [m3]
    
    Ares - coil area [m2]
    
    QV - coil heat per volume [W/m3]
    
    QA - coil heat per area [W/m2]
    
    '''
    Air_m = ct.Solution('air.xml')
    
    def __init__(self,n,massFlow,T_out,h,d,D,amb_Temp=21.0,Tmax=1000.0,p=0.01,Ap=8.9076535e-4):
        self.n = n
        self.massFlow = massFlow
        self.T_out = T_out
        self.amb_Temp = amb_Temp
        self.T_mean = (T_out-amb_Temp)/2.0

        self.Air_m.TP = self.T_mean+273, ct.one_atm
        self.cp = self.Air_m.cp
        self.Q = self.massFlow*self.cp*(self.T_out-self.amb_Temp)
        self.q = self.Q/self.n        
        
        
        self.h = h
        self.d = d
        self.D = D
        self.p = p
        self.Ap = Ap
        self.A = (self.q/(self.h*(Tmax-self.T_out)))
        self.L = self.A/(np.pi*self.d)
        self.N = self.A/(np.pi*self.d*0.094746)
        self.l = self.N*self.p        
        
        self.R = float(A1prop.kanthal_resistance[A1prop.kanthal_diam==self.d])*self.L*self.n
        self.I = np.sqrt(self.q/self.R)
        self.U = self.R*self.I

        self.Vres = (np.pi/4.*self.d**2)*self.L
        self.qV = self.q/self.Vres
        self.qA = self.q/self.A
        
        
        
    def report_Res(self):
        print('\n*****************')
        print('Resistance infos.\n')
        print('Total Heat (mdot cp dT): ' + '{:.2f}'.format(self.Q) + ' [W]')
        print('Heat each passage: ' + '{:.2f}'.format(self.q) + ' [W]')
        print('Mass flow each passage:' + '{:.2e}'.format(self.massFlow/self.n) + ' [kg/s]')
        print('\n-COIL (each):\n--Heat Transfer Area: ' + '{:.4e}'.format(self.A) + ' [m2]')
        print('--Stretched wire: ' + '{:.2f}'.format(self.L) + ' [m]')
        print('--length: ' + '{:.2f}'.format(self.l) + ' [m]')
        print('--pitch: ' + '{:.2f}'.format(self.p) + ' [m]')
        print('--N turns: ' + '{:.0f}'.format(self.N) + ' [-]')
        print('--Q/V: ' + '{:.3f}'.format(self.qV) + ' [W/m3]')
        print('--Q/A: ' + '{:.3f}'.format(self.qA) + ' [W/m2]')
        print('\n-Voltage: ' + '{:.2f}'.format(self.U) +' [V]')
        print('-Resistance: ' + '{:.2f}'.format(self.R) + ' [Ohms]')
        print('-Current: ' + '{:.2f}'.format(self.I) + ' [A]')
        print('*****************')
        
        return 'end'