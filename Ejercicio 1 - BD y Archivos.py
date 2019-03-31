# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 18:41:38 2019

@author: Diego
"""

import pymssql

server = 'monostematicos.com'
user = 'hernan'
password = 'mage'
base = 'beta-ori_sistema'
dni = '29552719'

conn = pymssql.connect(server, user, password, base)
cursor = conn.cursor()

cursor.execute('SELECT * FROM padron WHERE dni = %s', dni)
row = cursor.fetchone()
if row:
    print('DNI {0} encontrado! Escribiendo archivo'.format(dni))
    f = open(dni + ".txt", "w")
    f.writelines("INFORME PARA DNI {0}\n".format(dni))
    f.writelines("\n")
    f.writelines("NOMBRE: {0}\n".format(row[1]))
    f.writelines("APELLIDO: {0}\n".format(row[2]))
    f.writelines("CALLE: {0}\n".format(row[3]))
    f.writelines("DISTRITO: {0}\n".format(row[4]))
    f.writelines("SEXO: {0}\n".format(row[5]))
    f.close()
    print(row)
    
    print('Listo.')
else:
    print('DNI {0} no encontrado!'.format(dni))

conn.close()