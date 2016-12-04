#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import numpy as np
import csv
import matplotlib.pyplot as plt
import scipy.signal as sig
#import OFIO

msg1 = '\nCalcula a PSD do sinal'
msg2 = '\nModo de uso (argumentos):\n1-Nome do arquivo com o sinal'
msg2 += '\n2-Nome para o caso'

try:
    if sys.argv[1] == '-h':
        print msg1+msg2
        
except:
    pass

try:
    arquivo = sys.argv[1]
except:
    arquivo = input('Digite o nome do arquivo com o sinal: ')
    
try:
    namecase = sys.argv[2]
except:
    namecase = raw_input('Digite o nome do caso: ')

with open(arquivo,'rb') as csvfile:
    spreadsheet = csv.reader(csvfile, delimiter=',')
    
    tableList = []

    for row in spreadsheet:
        tableList.append(row)

header = tableList[0]
tableList = tableList[1:]

data = np.asarray(tableList).astype(np.float)

magU = np.zeros(len(tableList))
magU = data[:,27]

u = data[:,3]
v = data[:,10]
w = data [:,17]

meanU = np.mean(magU)
meanu = np.mean(u) 
meanv = np.mean(v)
meanw = np.mean(w)

meanuL = magU - meanU
uL = u - meanu
vL = v - meanv
wL = w - meanw

meanuLpad = np.pad(meanuL,len(meanuL),'constant',constant_values=0.0)
uLpad = np.pad(uL,len(uL),'constant',constant_values=0.0)
vLpad = np.pad(vL,len(vL),'constant',constant_values=0.0)
wLpad = np.pad(wL,len(wL),'constant',constant_values=0.0)

time = np.zeros_like(magU)
time = data[:,-1]

plt.figure()
plt.subplot(211)
plt.plot(time,meanuL,label='magU\'')
plt.title(str(namecase))
plt.xlabel('s');plt.ylabel('m/s')
plt.legend()
plt.subplot(212)
plt.plot(time,uL,'r',label='u\'')
plt.plot(time,vL,'g',label='v\'')
plt.plot(time,wL,'c',label='w\'')
plt.xlabel('s');plt.ylabel('m/s')
plt.legend()

ucorr = np.correlate(meanuL,meanuL,mode='full')

fft = np.fft.rfft(ucorr)
fft = fft[1:]
freq = np.fft.fftfreq(ucorr.size)
freq = freq[freq>0.0]
magfft = np.abs(fft)
PSD = np.square(magfft)

freqw,welch = sig.welch(uL, fs=1.0, window='nuttall', nperseg=256,
                     noverlap=20, nfft=1024,scaling='density')

freqw = freqw*len(uL)/(2*np.pi)

plt.figure()
plt.plot(freqw,welch)
plt.title(str(namecase))
plt.ylabel('PSD');plt.xlabel('freq')
plt.yscale('log');plt.xscale('log')
plt.show()