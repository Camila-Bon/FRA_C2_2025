#mayor y su posición (sin usar max)
n = 7
numeros = [0] * n

for i in range(n):
    numeros[i] = int(input(f"Ingrese el valor {i+1}: "))

valor_max = numeros[0]
posicion = 0

for i in range(1, n):
    if numeros[i] > valor_max:
        valor_max = numeros[i]
        posicion = i

print("El valor más grande es:", valor_max)
print("Está en la posición:", posicion)
