# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 01:49:04 2019

@author: Diego
"""

import MatrixNeuralNetworks
import Simulador_de_tateti
import uuid
import random
import datetime

def proxyIAfunc(self, tablero, equipo):
    return self.otra_data[0].procesar(tablero, equipo)

class NNTateti(MatrixNeuralNetworks.NeuralNetwork):
    def __init__(self):
        # Creo la red neuronal
        super(NNTateti, self).__init__(18, [14, 12], 9, MatrixNeuralNetworks.SeudoSigmoidActivation)
        # Le asigno un ID para identificarla
        self.ID = uuid.uuid4().hex[:8]
        #print('Se creó una IA con ID = ' + self.__ID)
        super(NNTateti, self).randomizeNeuralNetwork()
        
        self.edad = 0
        self.mutaciones = 0

    def deriveNNTateti(self):
        newNN = NNTateti()
        
        '''
        for layer in range(1, len(self.layers)):
            for neuron in range(len(self.layers[layer])):
                newNN.layers[layer][neuron].bias = self.layers[layer][neuron].bias + random.randrange(-1, 2) * 0.2
        '''
        for axonlayer in range(len(self.axons)):
            for axonlist in range(len(self.axons[axonlayer])):
                for i in range(len(self.axons[axonlayer][axonlist])):
                    newNN.axons[axonlayer][axonlist][i] = self.axons[axonlayer][axonlist][i] + random.randrange(-10, 11) * 0.05
        newNN.edad = self.edad
        newNN.mutaciones = self.mutaciones + 1
        return newNN
    
    # devuelve una lista de movidas que haría
    def procesar(self, unTablero, miFicha):
        fichasAjenas = unTablero.copy()
        fichasPropias = unTablero.copy()
        for i in range(len(unTablero)):
            if unTablero[i] != miFicha:
                fichasAjenas[i] = 1
            else:
                fichasAjenas[i] = 0
            if unTablero[i] == miFicha:
                fichasPropias[i] = 1
            else:
                fichasPropias[i] = 0
        fichasAjenas.extend(fichasPropias)
        entrada = fichasAjenas
        
        salida = super(NNTateti, self).Calcular(entrada)
        salidax = []
        
        # transformo la salida de una lista de posibilidades a una lista de tuplas
        # donde el primer valor es la posibilidad, y el segundo, la posición
        for i in range(len(salida)):
            salidax.append([salida[i], i])
        
        # Ahora ordeno las preferencias de mayor a menor
        salidax.sort(key=lambda x: x[0], reverse=True)
        
        # Devuelve para el resultado solo casillas no ocupadas
        res = []
        for respuesta in salidax:
            #f unTablero[respuesta[1]] == ' ':
                res.append(respuesta[1])
        if len(res) == 0:
            print('ATENCION! La salida calculada es nula!')
            print('Tablero: ' + str(unTablero))
            print('Salida: ' + str(salidax))
            print('res: ' + str(res))
        return res

class tatetiArena:
    def __init__(self, cantidadIAs):
        self.ListaNNs = []
        
        for i in range(cantidadIAs):
            self.ListaNNs.append(NNTateti())
    
    # Devuelve -1 si ganó la primer IA, 0 si empataron y 1 si ganó la segunda
    # En el segundo parámetro devuelve la cantidad de movidas hechas    
    def __enfrentar(self, unaIA, otraIA):
        #print('  ' + unaIA.ID + ' vs ' + otraIA.ID)
        jugador1 = Simulador_de_tateti.Jugador(False, proxyIAfunc, [unaIA]) 
        jugador2 = Simulador_de_tateti.Jugador(False, proxyIAfunc, [otraIA]) 
        resPartida, cantMov = Simulador_de_tateti.simular_partido_tateti([jugador1, jugador2])

        res = 0
        if resPartida == 0:
            res = -1
            #print('  Ganó ' + unaIA.ID)
        elif resPartida == 1:
            res = 1
            #print('  Ganó ' + otraIA.ID)
        #else:
            #print('  Empate')

        return res, cantMov
    
    def SalvarIAs(self):
        for i in range(len(self.ListaNNs)):
            f = open('IAs/IA' + str(i) + '.txt', 'w')
            f.write(self.ListaNNs[i].toString() + '\n')
            f.write('ID:' + self.ListaNNs[i].ID + '\n')
            f.write('Edad:' + str(self.ListaNNs[i].edad) + '\n')
            f.write('Mutaciones:' + str(self.ListaNNs[i].mutaciones) + '\n')
            f.close()
        
    def EvolucionarIAs(self):
        for i in range(len(self.ListaNNs)):
            self.ListaNNs[i].puntaje = 0
            self.ListaNNs[i].victorias = 0
            self.ListaNNs[i].derrotas = 0
            self.ListaNNs[i].empates = 0
            self.ListaNNs[i].edad = self.ListaNNs[i].edad + 1
        
        start = datetime.datetime.now()        
        
        # Todas las IAs se enfrentan con todas
        for i in range(len(self.ListaNNs)):
            #print('Ronda ' + str(i) + ' de ' + str(len(self.ListaNNs)))
            for j in range(len(self.ListaNNs)):
                #print('Partida ' + str(j) + ' de ' + str(len(self.ListaNNs)))
                if i != j:
                    res, mov = self.__enfrentar(self.ListaNNs[i], self.ListaNNs[j])
                    
                    # ganó la primer IA
                    if res == -1:
                        # ganar no es meritorio en tateti, de todos modos le sumamos unos puntitos
                        #self.ListaNNs[i].puntaje = self.ListaNNs[i].puntaje + 0.1
                        # perder es muy malo, y si fue en menos de 9 jugadas, peor
                        self.ListaNNs[j].puntaje = self.ListaNNs[j].puntaje - 1 #self.ListaNNs[i].edad # (10 - mov)
                        #self.ListaNNs[i].puntaje = self.ListaNNs[i].puntaje + self.ListaNNs[j].edad 
                        self.ListaNNs[i].victorias = self.ListaNNs[i].victorias + 1
                        self.ListaNNs[j].derrotas = self.ListaNNs[j].derrotas + 1
                    elif res == 1:
                        # Misma historia, pero a la inversa
                        #self.ListaNNs[j].puntaje = self.ListaNNs[j].puntaje + 0.1
                        self.ListaNNs[i].puntaje = self.ListaNNs[i].puntaje - 1 #self.ListaNNs[j].edad #(10 - mov)
                        #self.ListaNNs[j].puntaje = self.ListaNNs[j].puntaje + self.ListaNNs[i].edad
                        self.ListaNNs[j].victorias = self.ListaNNs[j].victorias + 1
                        self.ListaNNs[i].derrotas = self.ListaNNs[i].derrotas + 1
                    else:
                        # Vamos a darle puntos por empatar igual a la edad de la otra neurona
                        # tiene mucho mérito empatar con un sobreviviente
                        #self.ListaNNs[i].puntaje = self.ListaNNs[i].puntaje + self.ListaNNs[j].edad * .5
                        #self.ListaNNs[j].puntaje = self.ListaNNs[j].puntaje + self.ListaNNs[i].edad * .5
                        
                        self.ListaNNs[i].empates = self.ListaNNs[i].empates + 1
                        self.ListaNNs[j].empates = self.ListaNNs[j].empates + 1
                        
        end = datetime.datetime.now()
        elapsed = end - start
        print('La ronda tomó: ', elapsed) 
        
        
        # Luego de enfrentadas todas, ordenamos según puntaje
        self.ListaNNs.sort(key=lambda x: x.puntaje, reverse=True)
        
        # por propósitos de debug
        topten = []
        print('-------TOP TEN------')
        for i in range(10):
            print(str(i) + ') ptos:' + str(round(self.ListaNNs[i].puntaje, 2)).ljust(4) + ' edad:' + str(self.ListaNNs[i].edad).ljust(5) + ' v:' + str(self.ListaNNs[i].victorias).rjust(3) + ' e:' + str(self.ListaNNs[i].empates).rjust(3) + ' d:' + str(self.ListaNNs[i].derrotas).rjust(3) + ' ' + self.ListaNNs[i].ID + '.' + str(self.ListaNNs[i].mutaciones))
            topten.append(str(round(self.ListaNNs[i].puntaje, 2)) + ' edad:' + str(self.ListaNNs[i].edad) + ' v:' + str(self.ListaNNs[i].victorias) + ',e:' + str(self.ListaNNs[i].empates) + ',d:' + str(self.ListaNNs[i].derrotas))
        
        #print('Top ten: ' + str(topten))
        
        # ahora, mantengo como está al 10% superior de las IAs
        # 20% - se mantienen
        # 30% - se evolucionan4
        # 20% - se evolucionan a partir del top 20% (es decir, se reproducen)
        # 30% - se crean nuevas
        cant = len(self.ListaNNs)
        sesalvan = (cant * 10) // 100 # 5
        mutan = sesalvan + (cant * 30) // 100 # 20
        hijascampeones = mutan + sesalvan // 100 # 25
        #print(str(cant) + ',' + str(sesalvan) + ',' + str(mutan) + ',' + str(hijascampeones))
        for i in range(cant):
            if (i > sesalvan)  and (i <= mutan):
                self.ListaNNs[i] = self.ListaNNs[i].deriveNNTateti()
            elif (i > mutan) and (i <= hijascampeones):
                self.ListaNNs[i] = self.ListaNNs[i - mutan - 1].deriveNNTateti()
            elif (i > hijascampeones):
                self.ListaNNs[i] = NNTateti()    
'''                
        diezporciento = len(self.ListaNNs) // 10
        for i in range(diezporciento * 3):
            self.ListaNNs[len(self.ListaNNs) - 1 - i] = NNTateti()
        for i in range(diezporciento * 2):
            self.ListaNNs[len(self.ListaNNs) - 1 - diezporciento * 3 - i] = self.ListaNNs[i].deriveNNTateti()
        for i in range(diezporciento * 3):
            self.ListaNNs[len(self.ListaNNs) - 1 - diezporciento * 5 - i] = self.ListaNNs[len(self.ListaNNs) - 1 - diezporciento * 5 - i].deriveNNTateti()
        
'''



miArena = tatetiArena(50)
miArena.SalvarIAs()
for i in range(10000):
    print('======RONDA ' + str(i) + '=========')
    miArena.EvolucionarIAs()
    if i % 10 == 0:
        print('---Salvando backup---')
        miArena.SalvarIAs()
miArena.SalvarIAs()

