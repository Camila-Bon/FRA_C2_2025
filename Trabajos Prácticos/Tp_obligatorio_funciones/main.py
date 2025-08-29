from funciones.acceso import verificar_acceso
from funciones.area_triangulo import area_triangulo
from funciones.buscar_mayor import buscar_mayor
from funciones.calcular_edad import calcular_edad
from funciones.minutos import convertir_minutos
from funciones.operaciones import operaciones
from funciones.par_impar import es_par
from funciones.saludar import saludar


#1
nombre = input("Ingresar nombre: ")
saludar.saludar(nombre)

#2
n1 = int(input("Ingresar primer número: "))
n2 = int(input("Ingresar segundo número: "))
operaciones.operaciones(n1, n2)

#3
base = float(input("Ingresar base del triángulo: "))
altura = float(input("Ingresar altura del triángulo: "))
area_triangulo.area_triangulo(base, altura)

#4
a = int(input("Ingresar primer número: "))
b = int(input("Ingresar segundo número: "))
c = int(input("Ingresar tercer número: "))
buscar_mayor.buscar_mayor(a, b, c)

#5
num = int(input("Ingresar un número: "))
es_par.es_par(num)

#6
minutos = int(input("Ingresar minutos: "))
convertir_minutos.convertir_minutos(minutos)

#7
edad = int(input("Ingresar edad: "))
verificar_acceso.verificar_acceso(edad)

#8
año = int(input("Ingresar año de nacimiento: "))
año_actual = int(input("Ingresar año actual: "))
calcular_edad.calcular_edad(año, año_actual)
