#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import invariantes
import symAntisym
import saidaTela
import Tnormcis

## ========================================================================== ##
## ========================================================================== ##

T = np.array([[0,1,2],
              [1,2,0],
              [2,0,3]])

coordenadas = 'cartesianas' # 'cartesianas' 'cilindricas' ou 'esfericas'

plano = np.array([1,3,1])

## ========================================================================== ##
## ========================================================================== ##

## -- Calculo dos invariantes do tensor T -- ##
I = invariantes.calc(T)

## -- Calculo dos auto valores e vetores do tensor T -- ##
val,vet = np.linalg.eig(T)

## -- Calculo da parte simetrica e anti simetrica do tensor T -- ##
D,W = symAntisym.calc(T)

## -- Calculo do vetor tensao e tensoes normal e cisalhante no plano -- ##
t,Tn,tal = Tnormcis.calc(T,plano)

## -- Imprimi na tela os resultados -- ##
saidaTela.out(T,coordenadas,I,val,vet,D,W,plano,t,Tn,tal)