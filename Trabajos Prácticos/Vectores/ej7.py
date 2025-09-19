#invertir orden
n = 6
numeros = [0] * n

for i in range(n):
    numeros[i] = int(input(f"Ingrese el valor {i+1}: "))

print("Array invertido:")
for i in range(n, 0, -1):   # arranca en n, termina en 1
    print(numeros[i-1])     # accede al índice correcto
