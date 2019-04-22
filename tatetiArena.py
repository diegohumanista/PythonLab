# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 01:49:04 2019

@author: Diego
"""

import NeuralNetworks
import Simulador_de_tateti
import uuid
import random

def proxyIAfunc(self, tablero, equipo):
    return self.otra_data[0].procesar(tablero, equipo)

class NNTateti(NeuralNetworks.NeuralNetwork):
    def __init__(self):
        # Creo la red neuronal
        super(NNTateti, self).__init__(18, [27, 18, 15], 9, NeuralNetworks.DummyActivacion)
        # Le asigno un ID para identificarla
        self.ID = uuid.uuid4().hex
        #print('Se creó una IA con ID = ' + self.__ID)
        super(NNTateti, self).randomizeNeuralNetwork()

    def deriveNNTateti(self):
        newNN = NNTateti()
        
        for layer in range(1, len(self.layers)):
            for neuron in range(len(self.layers[layer])):
                newNN.layers[layer][neuron].bias = self.layers[layer][neuron].bias + random.randrange(-1, 2) * 0.1
        for axonlayer in range(len(self.axons)):
            for axonlist in range(len(self.axons[axonlayer])):
                for i in range(len(self.axons[axonlayer][axonlist])):
                    newNN.axons[axonlayer][axonlist][i] = self.axons[axonlayer][axonlist][i] + random.randrange(-1, 2) * 0.01
        
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
        
        # transformo la salida de una lista de posibilidades a una lista de tuplas
        # donde el primer valor es la posibilidad, y el segundo, la posición
        for i in range(len(salida)):
            salida[i] = [salida[i], i]
        
        # Ahora ordeno las preferencias de mayor a menor
        salida.sort(key=lambda x: x[0], reverse=True)
        
        # Devuelve para el resultado solo casillas no ocupadas
        res = []
        for respuesta in salida:
            #if unTablero[respuesta[1]] == ' ':
                res.append(respuesta[1])
        if len(res) == 0:
            print('ATENCION! La salida calculada es nula!')
            print('Tablero: ' + str(unTablero))
            print('Salida: ' + str(salida))
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
            f = open('IA' + str(i) + '.txt', 'w')
            f.write(self.ListaNNs[i].toString())
            f.close()
        
    def EvolucionarIAs(self):
        for i in range(len(self.ListaNNs)):
            self.ListaNNs[i].puntaje = 0
            
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
                        self.ListaNNs[i].puntaje = self.ListaNNs[i].puntaje + 0.1
                        # perder es muy malo, y si fue en menos de 9 jugadas, peor
                        self.ListaNNs[j].puntaje = self.ListaNNs[j].puntaje - (10 - mov)
                    elif res == 1:
                        # Misma historia, pero a la inversa
                        self.ListaNNs[j].puntaje = self.ListaNNs[j].puntaje + 0.1
                        self.ListaNNs[i].puntaje = self.ListaNNs[i].puntaje - (10 - mov)
        
        # Luego de enfrentadas todas, ordenamos según puntaje
        self.ListaNNs.sort(key=lambda x: x.puntaje, reverse=True)
        
        # por propósitos de debug
        topten = []
        for i in range(10):
            topten.append(round(self.ListaNNs[i].puntaje, 2))
        print('Top ten: ' + str(topten))
        
        # ahora, mantengo como está al 10% superior de las IAs
        # 20% - se mantienen
        # 30% - se evolucionan
        # 20% - se evolucionan a partir del top 20%
        # 30% - se crean nuevas
        diezporciento = len(self.ListaNNs) // 10
        for i in range(diezporciento * 3):
            self.ListaNNs[len(self.ListaNNs) - 1 - i] = NNTateti()
        for i in range(diezporciento * 2):
            self.ListaNNs[len(self.ListaNNs) - 1 - diezporciento * 3 - i] = self.ListaNNs[i].deriveNNTateti()
        for i in range(diezporciento * 3):
            self.ListaNNs[len(self.ListaNNs) - 1 - diezporciento * 5 - i] = self.ListaNNs[len(self.ListaNNs) - 1 - diezporciento * 5 - i].deriveNNTateti()
        




miArena = tatetiArena(50)
miArena.SalvarIAs()
for i in range(1000):
    miArena.EvolucionarIAs()
    if i % 100 == 0:
        miArena.SalvarIAs()

