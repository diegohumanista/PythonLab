import random

def TomarTirada():
    tirada = []
    vez = 1
    for x in range(5):
        tirada.append(random.randrange(1,7,1))
    
    print("Tu tirada es ", tirada)
    
    while (vez < 3) and (input("Deseas tirar de nuevo? (s/n) ") == "s"):
        cuales = input("Ingresa las posiciones de los dados que quieres cambiar (ej: 134) ")
        for x in cuales:
            try:
                lugar = int(x)-1
                if (lugar >= 0) and (lugar <= len(tirada)):
                    tirada[int(x)-1] = random.randrange(1,7,1)
                else:
                    print("El número ", x, " está fuera de rango")
            except ValueError:
                print(x, " no es un número, che")
        print("Tu nueva tirada es ", tirada)
        vez = vez + 1
    print("-------------------------")
    print("Tu tirada FINAL es ", tirada)

    return tirada    

def CalcularPuntaje(unaTirada):
    Resumen = [0, 0, 0, 0, 0, 0]
    Puntaje1 = 0;
    Puntaje2 = 0;
    Puntaje3 = 0;
    Puntaje4 = 0;
    for x in unaTirada:
        Resumen[x-1] = Resumen[x-1] + 1
    if Resumen.count(5) == 1:
        Puntaje1 = 8
        Puntaje2 = Resumen.index(5)
    elif Resumen.count(4) == 1:
        Puntaje1 = 6
        Puntaje2 = Resumen.index(4)
        Puntaje3 = Resumen.index(1)
    elif Resumen.count(3) == 1:
        if Resumen.count(2) == 1:
            Puntaje1 = 5
            Puntaje2 = Resumen.index(3)
            Puntaje3 = Resumen.index(2)
        else:
            Puntaje1 = 4
            Puntaje2 = Resumen.index(3)
            Puntaje3 = Resumen.index(1) 
            Resumen[Puntaje3] = 0
            Puntaje3 = Puntaje3 + Resumen.index(1)
    elif Resumen.count(2) == 2:
        Puntaje1 = 3
        Puntaje3 = Resumen.index(2) 
        Resumen[Puntaje3] = 0
        Puntaje2 = Resumen.index(2)
        Puntaje4 = Resumen.index(1)
    elif Resumen.count(2) == 1 and Resumen.count(3) == 0:
        Puntaje1 = 2
        Puntaje2 = Resumen.index(2)
        Puntaje3 = Resumen.index(1)
        Resumen[Resumen.index(1)] = 0
        Puntaje3 = Puntaje3 + Resumen.index(1)
        Resumen[Resumen.index(1)] = 0
        Puntaje3 = Puntaje3 + Resumen.index(1)
    elif Resumen.count(1) == 5:
        if Resumen.index(0) == 0 or Resumen.index(0) == 5:
            Puntaje1 = 7
            Puntaje2 = 6 - Resumen.index(0)
        else:
            Puntaje1 = 1
            Puntaje2 = 21 - (Resumen.index(0) + 1)
    
    return (Puntaje4 + Puntaje3 * 100 + Puntaje2 * 10000 + Puntaje1 * 1000000)

def ResultadoPartido(Tirada1, Tirada2):
    Puntaje1 = CalcularPuntaje(Tirada1)
    Puntaje2 = CalcularPuntaje(Tirada2)
    if Puntaje1 > Puntaje2:
        return 1
    else:
        if Puntaje2 > Puntaje1:
            return 2
        else:
            return 3

'''
j1 = input("Nombre del jugador 1: ")
j2 = input("Nombre del jugador 2: ")

print("JUEGA ", j1)
jugada1 = TomarTirada() # [1,4,5,2,1]

print("JUEGA ", j2)
jugada2 = TomarTirada()

Res = ResultadoPartido(jugada1, jugada2)

if Res == 1:
    print("Ganó ", j1)
else:
    if Res == 2:
        print("Ganó ", j2)
    else:
        print("Empataron!")
        
'''

Tirada1 = [6,6,6,6,6]
Tirada2 = [6,6,6,6,6]
print('Caso ', 1 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 3 else 'MAL')
Tirada1 = [5,5,5,5,5]
Tirada2 = [6,6,6,6,6]
print('Caso ', 2 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 2 else 'MAL')
Tirada1 = [4,4,4,4,4]
Tirada2 = [5,5,5,5,6]
print('Caso ', 3 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 1 else 'MAL')
Tirada1 = [3,3,3,3,3]
Tirada2 = [1,2,3,4,5]
print('Caso ', 4 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 1 else 'MAL')
Tirada1 = [2,2,2,2,2]
Tirada2 = [3,3,3,2,2]
print('Caso ', 5 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 1 else 'MAL')
Tirada1 = [2,2,2,2,2]
Tirada2 = [6,6,6,4,5]
print('Caso ', 6 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 1 else 'MAL')
Tirada1 = [1,1,1,1,1]
Tirada2 = [2,2,4,4,6]
print('Caso ', 7 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 1 else 'MAL')
Tirada1 = [2,2,2,2,2]
Tirada2 = [1,1,2,3,6]
print('Caso ', 8 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 1 else 'MAL')
Tirada1 = [3,3,3,3,3]
Tirada2 = [1,3,4,5,6]
print('Caso ', 9 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 1 else 'MAL')
Tirada1 = [1,2,3,4,5]
Tirada2 = [1,2,3,4,5]
print('Caso ', 10 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 3 else 'MAL')
Tirada1 = [1,2,3,4,5]
Tirada2 = [2,3,4,5,6]
print('Caso ', 11 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 2 else 'MAL')
Tirada1 = [1,2,3,4,5]
Tirada2 = [5,5,5,5,6]
print('Caso ', 12 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 1 else 'MAL')
Tirada1 = [1,2,3,4,5]
Tirada2 = [5,4,3,2,1]
print('Caso ', 13 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 3 else 'MAL')
Tirada1 = [1,2,3,4,5]
Tirada2 = [3,3,3,2,2]
print('Caso ', 14 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 1 else 'MAL')
Tirada1 = [1,2,3,4,5]
Tirada2 = [6,6,6,4,5]
print('Caso ', 15 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 1 else 'MAL')
Tirada1 = [1,2,3,4,5]
Tirada2 = [2,2,4,4,6]
print('Caso ', 15 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 1 else 'MAL')
Tirada1 = [1,2,3,4,5]
Tirada2 = [1,1,2,3,6]
print('Caso ', 16 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 1 else 'MAL')
Tirada1 = [1,2,3,4,5]
Tirada2 = [1,3,4,5,6]
print('Caso ', 17 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 1 else 'MAL')
Tirada1 = [5,5,5,5,4]
Tirada2 = [5,5,5,5,4]
print('Caso ', 18 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 3 else 'MAL')
Tirada1 = [4,4,4,4,5]
Tirada2 = [3,3,3,3,6]
print('Caso ', 19 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 1 else 'MAL')
Tirada1 = [4,4,4,4,5]
Tirada2 = [4,4,4,4,3]
print('Caso ', 20 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 1 else 'MAL')
Tirada1 = [4,4,4,4,5]
Tirada2 = [3,3,3,2,2]
print('Caso ', 21 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 1 else 'MAL')
Tirada1 = [4,4,4,4,5]
Tirada2 = [6,6,6,4,5]
print('Caso ', 22 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 1 else 'MAL')
Tirada1 = [4,4,4,4,5]
Tirada2 = [2,2,4,4,6]
print('Caso ', 23 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 1 else 'MAL')
Tirada1 = [4,4,4,4,5]
Tirada2 = [1,1,2,3,6]
print('Caso ', 24 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 1 else 'MAL')
Tirada1 = [4,4,4,4,5]
Tirada2 = [1,3,4,5,6]
print('Caso ', 25 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 1 else 'MAL')
Tirada1 = [4,4,4,5,5]
Tirada2 = [4,4,5,5,4]
print('Caso ', 26 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 3 else 'MAL')
Tirada1 = [3,3,3,5,5]
Tirada2 = [4,4,4,6,6]
print('Caso ', 27 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 2 else 'MAL')
Tirada1 = [3,3,3,5,5]
Tirada2 = [3,3,3,2,2]
print('Caso ', 28 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 1 else 'MAL')
Tirada1 = [3,3,3,5,5]
Tirada2 = [6,6,6,4,5]
print('Caso ', 29 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 1 else 'MAL')
Tirada1 = [3,3,3,5,5]
Tirada2 = [2,2,4,4,6]
print('Caso ', 30 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 1 else 'MAL')
Tirada1 = [3,3,3,5,5]
Tirada2 = [1,1,2,3,6]
print('Caso ', 31 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 1 else 'MAL')
Tirada1 = [3,3,3,5,5]
Tirada2 = [1,3,4,5,6]
print('Caso ', 32 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 1 else 'MAL')
Tirada1 = [5,5,5,1,2]
Tirada2 = [1,2,5,5,5]
print('Caso ', 33 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 3 else 'MAL')
Tirada1 = [5,5,5,1,2]
Tirada2 = [1,2,6,6,6]
print('Caso ', 34 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 2 else 'MAL')
Tirada1 = [5,5,5,1,2]
Tirada2 = [5,5,5,4,3]
print('Caso ', 35 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 2 else 'MAL')
Tirada1 = [5,5,5,1,2]
Tirada2 = [2,2,4,4,6]
print('Caso ', 36 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 1 else 'MAL')
Tirada1 = [5,5,5,1,2]
Tirada2 = [1,1,2,3,6]
print('Caso ', 37 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 1 else 'MAL')
Tirada1 = [5,5,5,1,2]
Tirada2 = [1,3,4,5,6]
print('Caso ', 38 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 1 else 'MAL')
Tirada1 = [1,1,2,2,3]
Tirada2 = [3,2,1,2,1]
print('Caso ', 39 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 3 else 'MAL')
Tirada1 = [5,5,1,1,2]
Tirada2 = [6,6,5,5,2]
print('Caso ', 40 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 2 else 'MAL')
Tirada1 = [4,4,1,1,3]
Tirada2 = [3,3,2,2,6]
print('Caso ', 41 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 1 else 'MAL')
Tirada1 = [4,4,3,3,2]
Tirada2 = [4,4,2,2,1]
print('Caso ', 42 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 1 else 'MAL')
Tirada1 = [2,2,1,1,5]
Tirada2 = [2,1,2,1,3]
print('Caso ', 43 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 1 else 'MAL')
Tirada1 = [2,2,1,1,5]
Tirada2 = [6,1,2,3,6]
print('Caso ', 44 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 1 else 'MAL')
Tirada1 = [2,2,1,1,5]
Tirada2 = [1,3,4,5,6]
print('Caso ', 45 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 1 else 'MAL')
Tirada1 = [5,5,4,6,1]
Tirada2 = [4,6,1,5,5]
print('Caso ', 46 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 3 else 'MAL')
Tirada1 = [5,5,4,6,1]
Tirada2 = [6,6,4,3,2]
print('Caso ', 47 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 2 else 'MAL')
Tirada1 = [5,5,4,6,1]
Tirada2 = [5,5,4,2,1]
print('Caso ', 48 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 1 else 'MAL')
Tirada1 = [5,5,4,6,1]
Tirada2 = [1,3,4,5,6]
print('Caso ', 49 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 1 else 'MAL')
Tirada1 = [6,6,5,3,2]
Tirada2 = [6,6,5,4,1]
print('Caso ', 50 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 3 else 'MAL')
Tirada1 = [5,5,5,3,2]
Tirada2 = [5,5,5,4,1]
print('Caso ', 51 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 3 else 'MAL')
Tirada1 = [1,3,4,5,6]
Tirada2 = [6,5,4,3,1]
print('Caso ', 52 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 3 else 'MAL')
Tirada1 = [1,3,4,5,6]
Tirada2 = [1,2,4,5,6]
print('Caso ', 53 , 'OK' if ResultadoPartido(Tirada1, Tirada2) == 1 else 'MAL')
