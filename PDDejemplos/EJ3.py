# -*- coding: utf-8 -*-
"""
@author: Vahar
"""
#paquetes
from itertools import takewhile

#Carrito: "Nombre del paquete", Kilos, Precio
def proceso_peso(item):
    nombre, peso, valor = item
    proceso_peso.peso_maximo -= peso
    return proceso_peso.peso_maximo >= 0   
def proceso_valor(item):
    nombre, peso, valor = item
    return float(valor)

#main
def main():
    mochila = (
    ("A", 1, 2), ("B", 2, 5), ("C", 4, 6), ("D", 5, 10),("E", 7, 13), ("F", 8, 17))

    #carga máxima del carrito
    proceso_peso.peso_maximo = 8

    #Cargas
    carga_lista = list(takewhile(proceso_peso, reversed(sorted(mochila, key=proceso_valor))))

    sumacarga = 0
    sumavalor = 0
    for item in carga_lista:
        print (item[0] + ' Peso :%i' % item[1] + ' valor :%i' % item[2])
        sumacarga = sumacarga + item[1]
        sumavalor = sumavalor + item[2]
    print ('')
    print ('Valor de objetos en la mochila: %i' % sumavalor)

main()
