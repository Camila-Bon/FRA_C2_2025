#-------------1--------------

nombre = input("ingrese su nombre: ")
print(f"Hola {nombre}")

edad = int(input("Ingrese su edad: "))

atracciones = int(input("Cuantas atracciones quiere usar? "))

#-------------2--------------

edad_atracciones = int(input("Verifique su edad para subir a las atracciones: "))

if edad_atracciones >= 12 and edad_atracciones <= 15:
    print("Se puede subir a la Montaña Rusa")
elif edad_atracciones < 6:
    print("Solo se puede subir al Carrusel")
else:
    print("Puede subirse a todas las atracciones!")

#-------------3--------------

precio_montaña_rusa = 1500
precio_casa_terror = 1200
precio_carrusel = 800

total_general = 0

while True:
    nombre = input("ingrese su nombre: ")
    print(f"Hola {nombre}")
    
    edad = int(input("Ingrese su edad: "))
    total_individual = 0  

    #4
    atracciones_elegidas = ""
    atracciones_usadas = ""

    #Montaña Rusa
    deseo = input("¿Quiere subir a la Montaña Rusa? (si/no): ")
    if deseo == "si":
        atracciones_elegidas += "Montaña Rusa"
        if 12 <= edad <= 15:
            print("Puede subir a la Montaña Rusa.")
            atracciones_usadas += "Montaña Rusa"
            total_individual += precio_montaña_rusa
        else:
            print("No puede subir a la Montaña Rusa.")

    #Casa del Terror
    deseo = input("¿Quiere entrar a la Casa del Terror? (si/no): ")
    if deseo == "si":
        atracciones_elegidas += "Casa del Terror"
        if edad >= 15:
            print("Puede entrar a la Casa del Terror.")
            atracciones_usadas += "Casa del Terror"
            total_individual += precio_casa_terror
        else:
            print("No puede entrar a la Casa del Terror.")

    #Carrusel
    deseo = input("¿Quiere subir al Carrusel? (si/no): ")
    if deseo == "si":
        atracciones_elegidas += "Carrusel"
        if edad <=6:
            print("Puede subir al Carrusel.")
            atracciones_usadas += "Carrusel"
            total_individual += precio_carrusel
        else:
            print("No puede subir al Carrusel.")

    #Resumen
    print("--- Resumen de la visita ---")
    print("Nombre:", nombre)

    print("Atracciones que quiso usar: ")
    if atracciones_elegidas != "":
        print(atracciones_elegidas)
    else:
        print("Ninguna")

    print("Atracciones que pudo usar: ")
    if atracciones_usadas != "":
        print(atracciones_usadas)
    else:
        print("Ninguna")

    print("Total a pagar: $", total_individual)

    #total del visitante
    print(f"Total a pagar por este visitante: ${total_individual}")
    total_general += total_individual 
    break 

#total final
print(f"Total general recaudado por todas las atracciones: ${total_general}")
