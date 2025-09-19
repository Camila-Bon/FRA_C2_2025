#cargar y mostrar array
n = 5
numeros = [0] * n

for i in range(n):
    numeros[i] = int(input(f"Ingrese el valor {i+1}: "))

print("Contenido del array:")
for i in range(n):
    print(numeros[i])
