#Tipos de datos
#Numéricos
#Entero (int)
variable_entera = 10
#Decimales (float)
variable_decimal = 2.5
#Cadenas de textp (str)
variable_cadena = "Hola Mundo!"
#Boolean
variable_booleana = True


nombre = input("ingrese su nombre: ")
print("Hola ", nombre)
print(f"Hola {nombre}")

edad = int(input("Ingrese edad: "))

if edad >= 18:
    print("Es mayor de edad...")
else:
    print("Es menor de edad...")

altura = float(input("Ingrese su altura: "))
#---------------------------------------
#combinar dos variantes y rangos
if altura >= 1.60 and altura < 1.80:
    print("Altura normal")
elif altura < 1.60:
    print("Altura baja")
elif altura >= 1.80 and altura < 2:
    print("Altura alta")
else: 
    print("Altura alta")

#--------------------------
if edad >= 18 and altura >= 1.80:
    print("La persona es mayor de edad y además es alta")

if edad >= 18 or altura >= 1.80:
    print("La persona puede ser mayor de edad o puede ser alta")

#-------------------------------------
numero_1 = int("ingrese un numero: ")
numero_2 = int("ingrese otro numero: ")

resultado_suma = numero_1 + numero_2
#las dos estan correctas. Estan bien las dos.
print(f"El resultado de la suma es: {resultado_suma}")

print(f"El resultado de la suma es: {numero_1 + numero_2}, y la resta es: {numero_1 - numero_2}") 
#si son cuentas cortas, podemos ponerlas en el str