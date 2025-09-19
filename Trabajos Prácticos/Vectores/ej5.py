#buscar un valor
n = 10
numeros = [0] * n

for i in range(n):
    numeros[i] = int(input(f"Ingrese el valor {i+1}: "))

buscado = int(input("Ingrese el número a buscar: "))

posicion = -1
for i in range(n):
    if numeros[i] == buscado:
        posicion = i
        break

if posicion != -1:
    print("El número", buscado, "está en la posición:", posicion)
else:
    print("El número no se encuentra en el array.")
