# dummy function used for input neurons
def DummyActivacion(aValue):
    return aValue

class Neuron:
    def __init__(self, aBias, anActivationFunction):
        self.bias = aBias
        self.__activationFunction = anActivationFunction

    def getBias(self):
        return self.__bias
    def setBias(self, aBias):
        self.__bias = aBias
    bias = property(getBias, setBias)
        
    def setInputValuesSum(self, inputValuesSum):
        self.__inputValuesSum = inputValuesSum
        self.__value = self.__activationFunction(self.__inputValuesSum + self.bias)
        
    def getValue(self):
        return self.__value
    value = property(getValue)
    
class NeuralNetwork:
    def __init__(self, inputCount, layersSizeList, outputCount, anActivationFunction):
        
        # Tracking layers sizes
        self.__layersSize = []
        self.__layers = []
        
        # Creating the input neurons
        inputLayer = []
        for x in range(inputCount):
            # Input neurons don't perform calculation, so we set a dummy function
            inputLayer.append(Neuron(0, DummyActivacion))

        self.__layers.append(inputLayer)
        self.__layersSize.append(inputCount)
        
        previousLayerCount = inputCount
        
        self.__axons = []
        
        for x in range(len(layersSizeList)):
            layer = []
            axonLayer = []
            for y in range(layersSizeList[x]):
                layer.append(Neuron(0, anActivationFunction))
                axonLayer.append([1] * previousLayerCount)
            previousLayerCount = layersSizeList[x]
            self.__layers.append(layer)
            self.__layersSize.append(layersSizeList[x]) 
            self.__axons.append(axonLayer)
                        
        outputNeurons = []
        axonLayer = []
        for x in range(outputCount):
            outputNeurons.append(Neuron(0, anActivationFunction))
            axonLayer.append([1] * previousLayerCount)
        self.__axons.append(axonLayer)
        self.__layers.append(outputNeurons)           
        self.__layersSize.append(outputCount)
        
        self.layers = self.__layers
        self.axons = self.__axons

   
    def Calcular(self, inputValuesList):
        if len(inputValuesList) != self.__layersSize[0]:
            print('Error, se están queriendo introducir {0} parametros cuando la red tiene {1}'.format(len(inputValuesList), self.__layersSize[0]))
        
        for x in range(len(inputValuesList)):
            self.__layers[0][x].setInputValuesSum(inputValuesList[x])
        
        for x in range(len(self.__layers)-1):
            for y in range(self.__layersSize[x+1]):
                calcValue = 0
                for z in range(self.__layersSize[x]):
                    calcValue = calcValue + self.__layers[x][z].value * self.__axons[x][y][z]
                self.__layers[x+1][y].setInputValuesSum(calcValue)
                
        result = []
        for x in range(self.__layersSize[-1]):
            result.append(self.__layers[-1][x].value)
        return result
    
def Activacion(valor):
    return valor




'''
miNeurona = Neuron(-1, Activacion)
miNeurona.setInputValuesSum(3)
print(miNeurona.value)
'''
'''
miRed = NeuralNetwork(1, [2], 1, Activacion)
print(miRed.Calcular([1]))

miRed = NeuralNetwork(2, [3], 1, Activacion)
print(miRed.Calcular([1,2]))

miRed.layers[1][0].bias = 2
miRed.layers[1][1].bias = 4
miRed.layers[1][2].bias = -5

miRed.layers[2][0].bias = 8

miRed.axons[0][0][0] = 0.5
miRed.axons[0][0][1] = 1.3

miRed.axons[0][1][0] = 0.3
miRed.axons[0][1][1] = 0.3

miRed.axons[0][2][0] = 0.2
miRed.axons[0][2][1] = 1.1

miRed.axons[1][0][0] = -1
miRed.axons[1][0][1] = 1
miRed.axons[1][0][2] = 0.8

print(miRed.Calcular([1,2]))
'''




