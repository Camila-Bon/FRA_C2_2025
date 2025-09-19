# comparar dos arrays
n = 5
vec1 = [0] * n
vec2 = [0] * n

print("Ingrese valores del primer array:")
for i in range(n):
    vec1[i] = int(input(f"Valor {i+1}: "))

print("Ingrese valores del segundo array:")
for i in range(n):
    vec2[i] = int(input(f"Valor {i+1}: "))

iguales = True
for i in range(n):
    if vec1[i] != vec2[i]:
        iguales = False
        break

if iguales:
    print("Los arrays son iguales.")
else:
    print("Los arrays no son iguales.")
