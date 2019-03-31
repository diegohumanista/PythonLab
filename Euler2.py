# Corresponde al ejercicio 2 de Project Euler
previo = 1
preprevio = 1
numero = 1
total = 0

while numero < 4000000:
    preprevio = previo
    previo = numero
    numero = numero + preprevio
    print(numero)
    if (numero % 2 == 0):
        total = total + numero
print ("el total es", total)