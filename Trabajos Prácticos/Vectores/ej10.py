#buscar primera aparición de un valor
def buscar_primera_aparicion(arreglo, numero):
    for i in range(len(arreglo)):
        if arreglo[i] == numero:
            return i
    return -1

n = int(input("Ingrese la cantidad de elementos del array: "))
numeros = [0] * n

for i in range(n):
    numeros[i] = int(input(f"Ingrese el valor {i+1}: "))

buscado = int(input("Ingrese el número a buscar: "))

pos = buscar_primera_aparicion(numeros, buscado)

if pos != -1:
    print("El número", buscado, "aparece primero en la posición:", pos)
else:
    print("El número no se encuentra en el array.")
