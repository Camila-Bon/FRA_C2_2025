#sumar todos los elementos
n = 10
numeros = [0] * n

for i in range(n):
    numeros[i] = int(input(f"Ingrese el valor {i+1}: "))

suma = 0
for i in range(n):
    suma += numeros[i]

print("La suma de los elementos es:", suma)
