#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 16:07:31 2016

@author: helio

Le arquivos de solucao do OpenFOAM na forma de NumPy array
"""

import re
import numpy as np
import os

class Read(object):
    '''Classe para ler campos resultados do OpenFOAM.
    
    Variaveis disponiveis:
    
        field: campo da variavel
    
        typeField: escalar|vetor
    
        nVol: quantidade de volumes da malha/tamanho vetor de campo
    
        time: timestep do campo lido

    '''
    def __init__(self,OFfile):
        self.OFfile = os.getcwd() + OFfile

        with open(self.OFfile,'r') as f:
            self.data = f.read()
    
        typeField = re.findall(r'List\<(\w*)\>', self.data)
        self.typeField = typeField[0]
        
        time = re.findall(r'location\s*"(\d*.\d*)', self.data)
        self.time = np.float(time[0])
        
        self.dimension = re.findall(r'dimensions\s*\[(.*)\]', self.data)
        
        nVol = re.findall(r'internalField.*\n(.*)', self.data)
        self.nVol = np.int(nVol[0])
        
        if self.typeField == 'scalar':
            self.field = re.findall(r'internalField.*\(\n(.*)\n\)\n;',self.data,re.MULTILINE+re.DOTALL)
            self.field = np.array(map(float,str(self.field[0]).split("\n")))
        else:
            self.field = re.findall(r'internalField.*\(\n\((.*)\)\n\)\n;',self.data,re.MULTILINE+re.DOTALL)
            self.field = str(self.field[0]).split(")\n(")
            for i,row in enumerate(self.field):
                self.field[i] = map(float,str(self.field[i]).split(" "))
                
            self.field = np.array(self.field)
            
class ProbesRead(object):
    '''Classe para ler data gerada pelo postProcess do OpenFOAM'''
    
    def __init__(self,OFfile):
        self.OFfile = os.getcwd() + '/postProcessing/probes/0/' + OFfile
        
        with open(self.OFfile,'r') as f:
            data_raw = f.read()
            
        self.data_raw = data_raw
        
        ## Separa header com comentarios
        data2 = self.data_raw.split("Time\n")[1]
        
        ## Divide linhas
        data2 = data2.split('\n')

        data = []
        
        ## Divide todos dados em uma matriz
        for i in data2:
            lines = i.strip()
            lines = lines.split()
            if lines!=[]:
                lines = map(float,lines)
                data.append(lines)
            else:
                print('\nWarning: Possible space between lines or at the EOF.\n')
            
        data = np.asarray(data)
        self.probes = np.transpose(data[:,1:])
        self.time = data[:,0]        
        