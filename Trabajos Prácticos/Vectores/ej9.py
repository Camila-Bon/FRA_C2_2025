#intercambiar elementos pares por ceros
n = 10
numeros = [0] * n

for i in range(n):
    numeros[i] = int(input(f"Ingrese el valor {i+1}: "))

for i in range(n):
    if numeros[i] % 2 == 0:
        numeros[i] = 0

print("Array resultante:")
for i in range(n):
    print(numeros[i])
