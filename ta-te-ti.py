# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 23:14:32 2019

@author: Diego
"""

class tateti:
    def __init__(self):
        self.__celdas = [' ', ' ', ' ', 
                       ' ', ' ', ' ',
                       ' ', ' ', ' ']
        self.__quienGano = ''
        self.__turno = ''
        
    def PonerX(self, posicion):
        if self.__turno == '':
            self.__turno = 'X'
        if self.__turno != 'X':
            print('No se puede poner X: es el turno de O')
            return False
        if self.hayGanador:
            print('No se puede poner X: ya hay un ganador')
            return False
        if self.__celdas[posicion] == ' ':
            self.__celdas[posicion] = 'X'
            self.__calcularGanador()
            self.__turno = 'O'
            return True
        else:
            print('No se puede poner X: casilla ocupada')
            return False
    def PonerO(self, posicion):
        if self.__turno == '':
            self.__turno = 'O'
        if self.__turno != 'O':
            print('No se puede poner O: es el turno de X')
            return False
        if self.hayGanador:
            print('No se puede poner O: ya hay un ganador')
            return False
        if self.__celdas[posicion] == ' ':
            self.__celdas[posicion] = 'O'
            self.__calcularGanador()
            self.__turno = 'X'
            return True
        else:
            print('No se puede poner O: casilla ocupada')
            return False
    def getHayGanador(self):
        return self.__quienGano != ''
    hayGanador = property(getHayGanador)
 
    def getQuienGano(self):
        return self.__quienGano
    quienGano = property(getQuienGano)

    def __calcularGanador(self):
        if self.__celdas[0] + self.__celdas[1] + self.__celdas[2] == 'OOO':
            self.__quienGano = self.__celdas[0]
        if self.__celdas[3] + self.__celdas[4] + self.__celdas[5] == 'OOO':
            self.__quienGano = self.__celdas[3]
        if self.__celdas[6] + self.__celdas[7] + self.__celdas[8] == 'OOO':
            self.__quienGano = self.__celdas[6]
        if self.__celdas[0] + self.__celdas[3] + self.__celdas[6] == 'OOO':
            self.__quienGano = self.__celdas[0]
        if self.__celdas[1] + self.__celdas[4] + self.__celdas[7] == 'OOO':
            self.__quienGano = self.__celdas[1]
        if self.__celdas[2] + self.__celdas[5] + self.__celdas[8] == 'OOO':
            self.__quienGano = self.__celdas[2]
        if self.__celdas[0] + self.__celdas[4] + self.__celdas[8] == 'OOO':
            self.__quienGano = self.__celdas[0]
        if self.__celdas[2] + self.__celdas[4] + self.__celdas[6] == 'OOO':
            self.__quienGano = self.__celdas[2]
 
        if self.__celdas[0] + self.__celdas[1] + self.__celdas[2] == 'XXX':
            self.__quienGano = self.__celdas[0]
        if self.__celdas[3] + self.__celdas[4] + self.__celdas[5] == 'XXX':
            self.__quienGano = self.__celdas[3]
        if self.__celdas[6] + self.__celdas[7] + self.__celdas[8] == 'XXX':
            self.__quienGano = self.__celdas[6]
        if self.__celdas[0] + self.__celdas[3] + self.__celdas[6] == 'XXX':
            self.__quienGano = self.__celdas[0]
        if self.__celdas[1] + self.__celdas[4] + self.__celdas[7] == 'XXX':
            self.__quienGano = self.__celdas[1]
        if self.__celdas[2] + self.__celdas[5] + self.__celdas[8] == 'XXX':
            self.__quienGano = self.__celdas[2]
        if self.__celdas[0] + self.__celdas[4] + self.__celdas[8] == 'XXX':
            self.__quienGano = self.__celdas[0]
        if self.__celdas[2] + self.__celdas[4] + self.__celdas[6] == 'XXX':
            self.__quienGano = self.__celdas[2]
         
        
    def __str__(self):
        return "[{} {} {}]\n[{} {} {}]\n[{} {} {}]".format(self.__celdas[0],self.__celdas[1],self.__celdas[2],self.__celdas[3],self.__celdas[4],self.__celdas[5],self.__celdas[6],self.__celdas[7],self.__celdas[8])
    def __repr__(self):
        return str(self)
'''
# para testear como funciona
p = tateti()
p.PonerO(1)
p.PonerX(3)
p.PonerO(4)
p.PonerX(5)
p.PonerO(7)
print(p)
print(p.hayGanador)
'''