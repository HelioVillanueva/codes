# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 12:39:31 2016

@author: helio
"""

from airHeater import preHeat,ct,np

## Ambient conditions
T_amb = 21 #[C]
p_amb = 101325 #[Pa]

mdot_air = 4.64e-3 #[kg/s]
mdot_fuel = 2.04e-4 #[kg/s]

r_AF = mdot_air/mdot_fuel


## Air at chamber inlet conditions
Tair_in = 600.0 #[C]

## Air properties
Air = ct.Solution('air.xml')
Air.TP = Tair_in+273, ct.one_atm
#Air()


## Fuel properties

# Natural gas (GRI3.0 dont have C4H10:0.0037,C5H12:0.0014 and C6H14:0.0006)
NG = ct.Solution('gri30.cti')
NG.TPX = T_amb+273, ct.one_atm, 'CH4:0.8826,C2H6:0.0799,C3H8:0.0188,N2:0.0065,CO2:0.0065'
#NG()

# Methane only
ch4 = ct.Solution('gri30.cti')
ch4.TPX = T_amb+273, ct.one_atm, 'CH4:1.,O2:2,N2:7.52'
ch4.equilibrate('TP')
#ch4()


## Electrical resistence properties
n = 4. # N of resistances/passages
h = 30.0 #[W/m2 K]
d = 0.003 #[m] wire diameter
D = 0.03 #[m] coil diameter

heater = preHeat(n,mdot_air,Tair_in,amb_Temp=T_amb,h=h,d=d,D=D)

print heater.report_Res()
