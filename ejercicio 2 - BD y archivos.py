# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 18:48:48 2019

@author: Diego
"""

import pymssql

server = 'monostematicos.com'
user = 'hernan'
password = 'mage'
base = 'beta-ori_sistema'
programador = 'Diego'

campos =  ('DNI', 'NOMBRE', 'APELLIDO', 'DIRECCION', 'DISTRITO', 'SEXO')
valores = ['',    '',       '',         '',          '',         '']
separadores = ('/', ':', '=', ' ')


f = open("archivo para leer.txt", "r")
fl = f.readlines()
for linea in fl:
    #print(linea)
    for c in campos:
        #print(c)
        if linea.upper().startswith(c):
            #print(c, ' encontrado en ', linea)
            if linea[len(c)] in separadores:
                #es un campo!!!
                valores[campos.index(c)] = linea[len(c)+1:].strip()
                #print(linea)

f.close()
print(valores)



conn = pymssql.connect(server, user, password, base)
cursor = conn.cursor()

cursor.execute('EXEC InsertarPersonaEnPadron %s, %s, %s, %s, %s, %s, %s', (campos[0], campos[1], campos[2], campos[3], campos[4], campos[5], programador))
row = cursor.fetchone()
if row:
    print('Resultado: {0}\n'.format(row[0]))

print('Listo.')
conn.close()
