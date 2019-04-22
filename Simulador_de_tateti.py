"""
=== USO: ===
1) Se crean dos Jugadores(esHumano, funcionIA, otra_data)
-> esHumano: 0 si es una IA y 1 si es un humano
-> funcionIA: la función que deberá usar la IA.
- Los argumentos son (self,tablero) refiriendose al jugador y a la lista con las 9 fichas del tablero
- Debe devolver una lista de 9 números, el mayor siendo el movimiento que más se quiere hacer, el segundo el que se quiere hacer si el primero no se puede, etc.
- Por defecto esta función devuelve todo 0 (es una IA muy mala)
-> otra_data: una lista con otra data que sea relevante
- Por defecto, una lista vacía: []
En teoría se le dará un otra_data con un objeto de red neuronal, y la funcionIA se limitará a darle el input a esta red neuronal
2) Se simula un partido usando simular_partido_tateti(Jugadores, mostrar, orden)
-> Jugadores: Una lista con los dos objetos Jugador que van a pelear
-> mostrar: Falso por defecto, si es True printeará el tablero y otros datos como el turno y el ganador a medida que avanza el juego.
-> orden: Es el orden de las fichas.
- Por defecto 'XO', quiere decir que juega X primero.
- 'OX' jugaría O primero. 'YJ' jugaría Y primero y después J (sí, se puede cambiar el tipo de ficha.. Creo que no rompe nada. Definitivamente no usen espacios. De hecho, ignoren esta funcionalidad, simplemente limítense a hacer que empiece el O si tienen ganas)
Esta función devuelve el jugador que ganó, 0 o 1
"""

import tateti

class Jugador:
    def __init__(self, esHumano = False, funcionIa = lambda a,b,c:[0]*9, otra_data = []):
        self.esHumano = esHumano
        self.funcionIa = funcionIa
        self.otra_data = otra_data #la data que sea necesaria para la IA
        
    def hacer_jugada(self, tablero, equipo):
        movimientos = [0] * 9
        if self.esHumano:
            movimiento = int(input("Elija dónde poner su ficha: "))
            while tablero[movimiento] != ' ':
                movimiento = int(input("Esa casilla está ocupada! Pruebe otra: "))
            movimientos[movimiento] = 1
        else:
            movimientos = self.funcionIa(self,tablero,equipo)
        return movimientos

def simular_partido_tateti(jugadores, mostrar = False, orden = 'XO'):
    cantMovimientos = 0
    tablero = tateti.tateti(orden)
    turno = 0
    if mostrar: print(str(tablero)+"\n")
    while not tablero.hayGanador:
        if mostrar: print("Turno de " + orden[turno])
        movimientos = jugadores[turno].hacer_jugada(tablero.getCeldas(),orden[turno])
        movimiento_nulo = min(movimientos)-1
        turnoRealizado = False
        movimiento = -1
        while not turnoRealizado:
            movimiento = movimientos.index(max(movimientos))
            movimientos[movimiento] = movimiento_nulo
            if tablero.getCeldas()[movimiento] == ' ':
                turnoRealizado = True
        tablero.PonerFicha(movimiento)
        cantMovimientos = cantMovimientos + 1
        if mostrar: print(str(tablero)+"\n")
        turno = 1-turno
    if mostrar: print("Ganó {}".format(tablero.quienGano))
    return orden.find(tablero.quienGano), cantMovimientos

"""
=== Para probar que funciona: ===

class supongamos_que_red_neuronal:
    def __init__(self,configuracion):
        self.configuracion = configuracion # los pesos y eso
    def procesar_input(self,input_dado,equipo):
        output = [4,1,7,
                  5,8,2,
                  6,0,3]
        return output
def funcion_ia_de_prueba(self,tablero,equipo):
    return self.otra_data[0].procesar_input(tablero,equipo)
mi_red_neuronal_falsa = supongamos_que_red_neuronal("configuración 100% legítima")
jugador1 = Jugador(False) #IA por defecto
jugador2 = Jugador(False,funcion_ia_de_prueba,[mi_red_neuronal_falsa]) #IA de testeo
print("Ganó el jugador {}".format(1+simular_partido_tateti([jugador1,jugador2],True)))
"""