#paquetes
from itertools import takewhile

#Carrito: "Nombre del paquete", Kilos, Precio
CARRITO = (
    ("Paquete 1", 9, 150), ("Paquete 2", 9, 160), ("Paquete 3", 153, 200), ("Paquete 4", 50, 160),
    ("Paquete 5", 15, 60), ("Paquete 6", 66, 45), ("Paquete 7", 27, 60), ("Paquete 8", 39, 40),
    ("Paquete 9", 230, 591), ("Paquete 10", 520, 10), ("Paquete 11", 110, 70), ("Paquete 12", 32, 30))

def proceso_valor(item):
    nombre, peso, valor = item
    return float(valor)

def proceso_peso(item):
    nombre, peso, valor = item
    proceso_peso.peso_maximo -= peso
    return proceso_peso.peso_maximo >= 0    

#carga máxima del carrito
proceso_peso.peso_maximo = 700

#Cargas
carga_lista = list(takewhile(proceso_peso, reversed(sorted(CARRITO, key=proceso_valor))))

sumacarga = 0
sumavalor = 0

for item in carga_lista:
    print (item[0] + ' Peso :%i' % item[1] + ' valor :%i' % item[2])
    sumacarga = sumacarga + item[1]
    sumavalor = sumavalor + item[2]

print ('')
print ('Peso total paquetes: %i' % sumacarga)
