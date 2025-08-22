#la cantidad de vueltas que va a dar de se define en tiempo de ejecucion - while
"""
a = 1
while a < 10:
    print (a)
    a += 2
"""
#contadores: +=
"""
contador = 0

while True:
    contador += 1
"""
    
#acumulador
#porcentajes
#promedios
#max y min

#Que es lo primero que hay que hacer cuando programamos un while true? ponerle la condición de corte (break)

#cuando no podemos saber de antemano cuantas vueltas va a dar hasta que funcione - while true. 
#ponerle condicion de corte, porque tiende a ser infinito.

#for. en que momento se define la cantidad de vueltas? en tiempo de 
#las vueltas se la damos nosotros- se puede usar "break" 
#nuestro primer numero es 0, no 1, los ciclos tambien

#range (). las vueltas con un numero; empeza en tal numero y termina en tal; q las vueltas las de en 2,4 o 6, etc.
#range(3); range(10, 20); range(10, 20, 2)

#for en decremento usando numero negativos. for i in range(4, -1- -1): print(i) = 4 3 2 1 0

#len: la cantidad de cosas tiene la lista?

#sentence continue: es cortar la vuelta. salta la vuenta y va a la otra. solo usando "continue"
#el break corta el ciclo.
#diferencia de "continue" y "break".

#---------------------------------------------------------------------

#### CODIGO EN CLASE
#CICLOS: for y while

#while

#numero = int(input("ingrese un numero: "))
#while numero < 100:   
 #   print(numero)
  #  numero = int(input("ingrese un numero: "))

#while numero < 100 and numero > 50:
 #   print(numero)
  #  numero = int(input("ingrese un numero: "))
"""
numero = int(input("ingresar numeros positivos: "))

if numero > 0:
    control = True

while control:
    numero = int(input("ingresar numeros positivos: "))
    if numero > 0:
        control = True
    else:
        control = False

contador_positivos = 0
contador_negativos = 0
numero = int(input("ingresar numeros, corta con 0: "))

while numero != 0:
    if numero > 0:
        contador_positivos += 1
    elif numero < 0:
        contador_negativos += 1

    numero = int(input("ingresar numeros, corta con 0: "))

total = 0

while True:
    monto = float(input("ingresar valor de producto: "))
    total += monto
    if monto == 0:
        break

#for
#tipos de in range()
#1
for x in range(3):
    nombre = input("ingresar nombre de mascota: ")
    tipo = input("que tipo de animal es? ")
    print(f"Animal {x + 1}, {nombre} es un {tipo}")

#2    
for x in range(1, 5):
    print(x + 1)

#3    
for x in range(0, 11, 2):
    print(x + 1)
#impar
#o
#par
for x in range(0, 11, 2):
    print(x)

"""
#listas. todavia no hay que ver pero esta en el ppt
lista = [1, 2, 3, 4, 5]

length = len(lista)

for i in range(length):
    index = length - i - 1
    print(lista[index])
 