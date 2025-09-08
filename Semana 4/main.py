#Vector de numeros.
vec_numeros = [0] * 5 

#vector de 5 elemetos que valen 0-

print(vec_numeros) #respuesta en terminal: [0, 0, 0, 0, 0]

#Vector de nombres.
vec_nombres = [""] * 5
#vector de decimales.
vec_decimales = [0.0] * 5

print(vec_nombres) #['', '', '', '', '']
print(vec_decimales) #[0.0, 0.0, 0.0, 0.0, 0.0]

#FUNCION LEN()
#la función len() nos retorna un entero que representa la cantidad de elementos_ 
#que tiene la estructura de datos que le pasemos como parámetro.
cantidad_elementos = len(vec_decimales) 

print(cantidad_elementos) #10


#cargar 5 notas de un alumno, mostrarlas; calcular el promedio y mostrarlo.
#carga de notas

for nota in range(len(vec_decimales)):

    vec_decimales[nota] = float(input("Ingresar nota: "))

#mostrar notas

for nota in range(len(vec_decimales)):
    print(f"Nota {nota + 1}: {vec_decimales[nota]}")

#promedio de notas
suma_notas = 0
for nota in range(len(vec_decimales)):
    suma_notas += vec_decimales[nota]

promedio_alumno = suma_notas / len(vec_decimales)

print(f"El promedio del alumno es: {promedio_alumno}")


#Hay tres instancias de estado en la materia: 1. Aprobado, 2. Regular, 3. Libre
#Se aprueba con promedio de >= 7. Regular con >= 4 y <= 6.99, abajo de 4 queda Libre.
#Pero para aprobar todas las calificaciones deben ser de 4 o más 

vec_estados = ["Aprobado", "Regular", "Libre"]

bandera_libre = False
estado = ""

for nota in range(len(vec_decimales)):
    if vec_decimales[nota] < 4:
        estado = vec_estados[2]
        bandera_libre = True
        break 

if not bandera_libre:
    if promedio_alumno >= 7:
        estado = vec_estados[0]
    elif promedio_alumno >= 4:
        estado = vec_estados[1]

print(f"El estado de alumno es: {estado}")


#--------------

vec_persona = ["Ana", 25, True]

print(vec_persona)

for elemento in range(len(vec_persona)):
    print(vec_persona[elemento])

#---------------

vec_persona[0] = "Juan"
vec_persona[2] = False

