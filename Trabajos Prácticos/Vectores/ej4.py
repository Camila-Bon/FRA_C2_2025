#contar mayores a 100
n = 8
numeros = [0] * n

for i in range(n):
    numeros[i] = int(input(f"Ingrese el valor {i+1}: "))

contador = 0
for i in range(n):
    if numeros[i] > 100:
        contador += 1

print("Cantidad de valores mayores a 100:", contador)
