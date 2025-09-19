#promedio 
n = 6
valores = [0.0] * n

for i in range(n):
    valores[i] = float(input(f"Ingrese el valor {i+1}: "))

suma = 0
for i in range(n):
    suma += valores[i]

promedio = suma / n
print("El promedio es:", promedio)
