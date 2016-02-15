#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def calc(tensor):
    D = 0.5*(tensor + np.transpose(tensor))    
    W = 0.5*(tensor - np.transpose(tensor))    
    return D, W