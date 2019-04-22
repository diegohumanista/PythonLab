class tateti:
    def __init__(self,orden = 'XO'):
        self.__celdas = [' ', ' ', ' ', 
                       ' ', ' ', ' ',
                       ' ', ' ', ' ']
        self.__quienGano = ''
        self.__fichas = orden
        self.__turno = orden[0]
    def PonerFicha(self, posicion):
        if self.hayGanador:
            print('No se puede poner ficha: ya hay un ganador')
            return False
        if self.__celdas[posicion] == ' ':
            self.__celdas[posicion] = self.__turno
            self.__calcularGanador()
            self.__turno = self.__fichas[self.__fichas.find(self.__turno)-1]
            return True
        else:
            print('No se puede poner ficha: casilla ocupada')
            return False
    def getHayGanador(self):
        return self.__quienGano != ''
    hayGanador = property(getHayGanador)
    def getQuienGano(self):
        return self.__quienGano
    quienGano = property(getQuienGano)
    def setQuienGano(self, val):
        self.__quienGano = val
    def getCeldas(self):
        return self.__celdas
    celdas = property(getCeldas)
    def reset(self):
        self.__celdas = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
        self.__quienGano = ''
        self.__turno = ''
    def partidaRapida(self, movidas): #Función de testeo
        for m in movidas:
            self.PonerFicha(m)
    def __calcularGanador(self):
        __array = [0,1,3,1,6,1,0,3,1,3,2,3,0,4,2,2] #Magia negra
        for n in range(8):
            init = __array[n*2]
            incr = __array[n*2+1]
            if (self.__celdas[init] == self.__celdas[init+incr] == self.__celdas[init+incr*2]) and (self.__celdas[init] != ' '):
                self.__quienGano = self.__celdas[__array[n*2]]
        if self.__quienGano == '' and not " " in self.__celdas:
            self.__quienGano = "Empate"
    def __str__(self):
        return "[{} {} {}]\n[{} {} {}]\n[{} {} {}]".format(self.__celdas[0],self.__celdas[1],self.__celdas[2],self.__celdas[3],self.__celdas[4],self.__celdas[5],self.__celdas[6],self.__celdas[7],self.__celdas[8])
    def __repr__(self):
        return str(self)