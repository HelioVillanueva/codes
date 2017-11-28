# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import numpy.random as npr
from scipy import optimize


class Neural_Network(object):
    def __init__(self, X, y):
        # Inputs X - control variables, y - values
        self.X = X/np.amax(X)
        self.y = y/y.max()
        
        # Define hyperparameters
        self.inputLayerSize = X.shape[1]
        self.outputLayerSize = y.shape[1]
        self.hiddenLayerSize = 3
        
        # weights (Parameters)
        self.W1 = npr.randn(self.inputLayerSize,self.hiddenLayerSize)
        self.W2 = npr.randn(self.hiddenLayerSize,self.outputLayerSize)
        
    def forward(self, X):
        # Propagate inputs through network
        self.z2 = np.dot(X, self.W1)
        self.a2 = self.sigmoid(self.z2)
        self.z3 = np.dot(self.a2, self.W2)
        yHat = self.sigmoid(self.z3)
        return yHat
    
    def sigmoid(self, z):
        # Apply sigmoid activation code
        return 1./(1.+np.exp(-z))
    
    def sigmoidPrime(self, z):
        # Derivative of Sigmoid Function
        return np.exp(-z)/((1.+np.exp(-z))**2.)

    def costFunction(self, X, y):
        #Compute cost for given X,y, use weights already stored in class.
        self.yHat = self.forward(X)

        return 0.5*sum((y-self.yHat)**2.)
    
    def costFunctionPrime(self, X, y):
        #Compute derivative with respect to W1 and W2
        self.yHat = self.forward(X)
        
        delta3 = np.multiply(-(y-self.yHat), self.sigmoidPrime(self.z3))
        dJdW2 = np.dot(self.a2.T, delta3)
        
        delta2 = np.dot(delta3, self.W2.T)*self.sigmoidPrime(self.z2)
        dJdW1 = np.dot(X.T, delta2)
        
        return dJdW1, dJdW2

    def computeGradients(self, X, y):
        dJdW1, dJdW2 = self.costFunctionPrime(X, y)
        return np.concatenate((dJdW1.ravel(), dJdW2.ravel()))
    
    #Helper functions for interacting with other methods/classes
    def getParams(self):
        #Get W1 and W2 Rolled into vector:
        params = np.concatenate((self.W1.ravel(), self.W2.ravel()))
        return params

    def setParams(self, params):
        #Set W1 and W2 using single parameter vector:
        W1_start = 0
        W1_end = self.hiddenLayerSize*self.inputLayerSize
        self.W1 = np.reshape(params[W1_start:W1_end], \
                             (self.inputLayerSize, self.hiddenLayerSize))
        W2_end = W1_end + self.hiddenLayerSize*self.outputLayerSize
        self.W2 = np.reshape(params[W1_end:W2_end], \
                             (self.hiddenLayerSize, self.outputLayerSize))

    def callbackF(self, params):
        self.setParams(params)
        self.J.append(self.costFunction(self.X, self.y))
        
    def costFunctionWrapper(self, params, X, y):
        self.setParams(params)
        cost = self.costFunction(X,y)
        grad = self.computeGradients(X,y)
        
        return cost, grad
        
    def train(self):

        #Make empty list to store costs:
        self.J = []
        
        params0 = self.getParams()

        options = {'maxiter': 200, 'disp' : True}
        _res = optimize.minimize(self.costFunctionWrapper, params0, jac=True, method='BFGS', \
                                 args=(self.X, self.y), options=options, callback=self.callbackF)

        self.setParams(_res.x)
        self.optimizationResults = _res
        
    def interpolate(self,X):
        return self.forward(X)*y.max()


#
#class Trainer(object):
#    def __init__(self, N):
#        #Make Local reference to network:
#        self.N = N
#        
#    def callbackF(self, params):
#        self.N.setParams(params)
#        self.J.append(self.N.costFunction(self.X, self.y))   
#        
#    def costFunctionWrapper(self, params, X, y):
#        self.N.setParams(params)
#        cost = self.N.costFunction(X,y)
#        grad = self.N.computeGradients(X,y)
#        
#        return cost, grad
#        
#    def train(self, X, y):
#        #Make an internal variable for the callback function:
#        self.X = X
#        self.y = y
#
#        #Make empty list to store costs:
#        self.J = []
#        
#        params0 = self.N.getParams()
#
#        options = {'maxiter': 200, 'disp' : True}
#        _res = optimize.minimize(self.costFunctionWrapper, params0, jac=True, method='BFGS', \
#                                 args=(X, y), options=options, callback=self.callbackF)
#
#        self.N.setParams(_res.x)
#        self.optimizationResults = _res






# Data
X = np.array(([0], [0.25], [0.5], [0.75]), dtype=float)

y = np.array(([1], [2], [3], [4]), dtype=float)

X2 = np.array(([0.5,0.5,0.2]), dtype=float)


NN = Neural_Network(X,y)

NN.train()

yHat = NN.interpolate(X)

print('Valores da tabela')
print(y)
print('Valores interpolados')
print(yHat)