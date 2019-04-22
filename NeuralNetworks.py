# dummy function used for input neurons
def DummyActivacion(aValue):
    return aValue

NN_HEADER_STRING = 'Neural Network'

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
    
    def toString(self):
        res = NN_HEADER_STRING + '\n' + \
            '  Network Inputs:' + str(self.__layersSize[0]) + '\n' + \
            '  Network Outputs:' + str(self.__layersSize[-1]) + '\n' + \
            '  Inner Layers:' + str(len(self.__layersSize)-2)  + '\n' + \
            '  Inner Layers sizes:' 
        for i in range(len(self.__layersSize)-2):
            if i != 0:
                res = res + ','
            res = res + str(self.__layersSize[i+1])
        res = res + '\n'
        for i in range(len(self.__layersSize)):
            if i == 0:
                res = res + '  Input Layer:\n'
            elif i == len(self.__layersSize) - 1:
                res = res + '  Output Layer:\n'
            else:
                res = res + '  Layer ' + str(i) + ':\n'    
            for j in range(self.__layersSize[i]):
                res = res + '    Neuron ' + str(j+1) + ':\n'
                res = res + '      Bias: ' + str(self.layers[i][j].bias) + '\n'
                res = res + '      Inputs:\n'
                if i == 0:
                    res = res + '        None\n'
                else:
                    for w in self.__axons[i-1][j]:
                        res = res + '        weight: ' + str(w) + '\n'
        res = res + 'End of description'
        return res
    
    def fromString(self, aString):
        inputs = 0
        outputs = 0
        innerlayers = 0
        innerlayerssizes = []
        initialized = False
        
        ActualLayer = None
        ActualNeuron = None
        ActualAxon = None
        
        sl = aString.splitlines()
        
        # si o si tiene que empezar con el header
        if sl[0] != NN_HEADER_STRING:
            raise ValueError('Not a valid Neural Network string')
        # Sacamos el header
        sl.pop(0)
        
        # procesamos el resto de la cadena
        while len(sl) != 0:
            linea = sl.pop(0).strip()

            # ignoramos las lineas vacías
            if linea == '':
                continue
            # Ignoramos los comentarios
            if linea[0] == '#':
                continue
            # tratamos de leer un parámetro
            params = linea.split(':')
            
            # si no hay, ignoramos la linea
            if len(params) == 1:
                continue

            params[0] = params[0].strip()
            params[1] = params[1].strip()
            
            if params[0] == 'Network Inputs':
                inputs = int(params[1])
                continue           
            if params[0] == 'Network Outputs':
                outputs = int(params[1])
                continue                  
            if params[0] == 'Inner Layers':
                innerlayers = int(params[1])
                continue         
            if params[0] == 'Inner Layers sizes':
                innerlayerssizes = params[1].split(',')
                for i in range(len(innerlayerssizes)):
                    innerlayerssizes[i] = int(innerlayerssizes[i].strip())
                continue
            
            # si ya tengo todos los parámetros que necesito por ahora, me voy
            if (inputs != 0) and (outputs != 0) and (innerlayerssizes != []) and not initialized:
                initialized = True
                print('Inicializando la red con ' + str(inputs) + ' entradas, ' + str(outputs) + ' salidas y ' + str(innerlayers) + ' capas intermedias ')
                # Con los datos que ya tengo, inicializo a la red
                self.__init__(inputs, innerlayerssizes, outputs, DummyActivacion)          
        
            if params[0] == 'Input Layer':
                ActualLayer = 0
                ActualNeuron = None
                ActualAxon = None
                continue           

            if params[0] == 'Output Layer':
                ActualLayer = innerlayers + 1
                ActualNeuron = None
                ActualAxon = None
                continue
            
            if params[0].startswith('Layer '):
                ActualLayer = int(params[0].split(' ')[1])
                ActualNeuron = None
                ActualAxon = None
                continue
            
            if params[0].startswith('Neuron '):
                ActualNeuron = int(params[0].split(' ')[1]) - 1
                ActualAxon = None
                continue
            
            if params[0] == 'Bias':
                ActualAxon = None
                print('Setting bias for neuron ' + str(ActualNeuron) + ' in layer ' + str(ActualLayer) + ' to ' + params[1])
                self.__layers[ActualLayer][ActualNeuron].bias = int(params[1])
                continue    

            if params[0] == 'Inputs':
                ActualAxon = 0
                continue
            
            if params[0] == 'weight':
                print('Setting axon\'s ' + str(ActualAxon) + ' weight for neuron ' + str(ActualNeuron) + ' in layer ' + str(ActualLayer) + ' to ' + params[1])
                self.__axons[ActualLayer-1][ActualNeuron][ActualAxon] = float(params[1])
                ActualAxon = ActualAxon + 1
                continue            
                


        # end while
    
def Activacion(valor):
    return valor




'''
miNeurona = Neuron(-1, Activacion)
miNeurona.setInputValuesSum(3)
print(miNeurona.value)
'''

'''
print('--------------Inicio--------------')
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

#print(miRed.toString())

miRed2 = NeuralNetwork(1, [1,1,1,1], 1, Activacion)
print(miRed2.toString())
print('---------------------------')
miRed2.fromString(miRed.toString())
print(miRed2.toString())
print('---------------------------')
print(miRed2.Calcular([1,2]))

'''





