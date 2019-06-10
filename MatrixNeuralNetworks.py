# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 19:52:38 2019

@author: Diego
"""

import numpy as np
import random

# dummy function used for input neurons
def DummyActivacion(aValue):
    return aValue

def IdentityActivation(aValue):
    return aValue

def BinaryStepActivation(aValue):
    if aValue < 0:
        return 0
    else:
        return 1

def SigmoidActivation(aValue):
    return 1 / (1 + np.exp(-aValue))

def SeudoSigmoidActivation(aValue):
    return aValue / (1 + np.abs(aValue))
    
def RareActivation(aValue):
    if aValue < 0:
        return aValue / 10
    else:
        return aValue


def TanhActivation(aValue):
    return np.tanh(aValue)

class NeuralNetwork:
    def __init__(self, inputCount, layersSizeList, outputCount, anActivationFunction):
        self.valores = []
        self.axons = []
        self.bias = []
        self.inputCount = inputCount
        self.outputCount = outputCount
        self.layersSizeList = layersSizeList

        self.activationFunction = np.vectorize(anActivationFunction)
        self.originalActivationFunction = anActivationFunction
        
        
        layersSizeList.append(outputCount)

        
        CapaAnterior = inputCount
        for x in layersSizeList:
            self.valores.append(np.zeros((x)))
            self.axons.append(np.ones((CapaAnterior, x)))
            self.bias.append(np.zeros((x)))
            CapaAnterior = x

    def Calcular(self, inputValuesList):
        if len(inputValuesList) != self.inputCount:
            print('Error, se están queriendo introducir {0} parametros cuando la red tiene {1}'.format(len(inputValuesList), self.inputCount))
        
        entrada = np.array(inputValuesList)
        
        for x in range(len(self.valores)):
            salida = self.activationFunction(np.dot(entrada, self.axons[x]) + self.bias[x])
            entrada = salida
        
        return salida
    
    def randomizeNeuralNetwork(self):
        # No randomizamos las neuronas input, por eso arranca de 1
        '''
        for x in range(len(self.bias)):
            for y in range(len(self.bias[x])):
                self.bias[x][y] = random.randrange(-30, 31) * 0.1
        '''


        for x in range(len(self.axons)):
            for y in range(len(self.axons[x])):
                for z in range(len(self.axons[x][y])):
                    self.axons[x][y][z] = random.randrange(-200, 201) * 0.01
 
    
    def deriveNeuralNetwork(self):
        newNN = NeuralNetwork(self.inputCount, self.layersSizeList, self.outputCount, self.originalActivationFunction)
        
        for x in range(len(newNN.bias)):
            for y in range(len(newNN.bias[x])):
                newNN.bias[x][y] = self.bias[x][y] + random.randrange(-1, 2) * 0.1
        

        for x in range(len(newNN.axons)):
            for y in range(len(newNN.axons[x])):
                for z in range(len(newNN.axons[x][y])):
                    newNN.axons[x][y][z] = self.axons[x][y][z] + random.randrange(-1, 2) * 0.1
       
        return newNN
    
    def fromString(self, aString):
        # Nada
        return
        
    def toString(self):
        # Nada
        return ''
    

            
#mnn = NeuralNetwork(1, [2], 1, DummyActivacion)
        '''
miRed = NeuralNetwork(2, [3], 1, DummyActivacion)
miRed.bias[0][0] = 2
miRed.bias[0][1] = 4
miRed.bias[0][2] = -5

miRed.bias[1][0] = 8

miRed.axons[0][0][0] = 0.5
miRed.axons[0][1][0] = 1.3

miRed.axons[0][0][1] = 0.3
miRed.axons[0][1][1] = 0.3

miRed.axons[0][0][2] = 0.2
miRed.axons[0][1][2] = 1.1

miRed.axons[1][0][0] = -1
miRed.axons[1][1][0] = 1
miRed.axons[1][2][0] = 0.8

print(miRed.Calcular([1,2]))
# me tiene que dar 5.72 '''