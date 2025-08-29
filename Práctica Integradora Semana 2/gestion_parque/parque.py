#Menú
def mostrar_atracciones():
    print("---Atracciones disponibles---")
    print("1. Montaña Rusa (Edad mínima: 12) - $1500")
    print("2. Carrusel (Edad: 6 o menos) - $800")
    print("3. Casa del Terror (Edad mínima: 15) - $1200")
    print("-----------------------------")

#Verificacion de edad
def puede_subir(edad, atraccion):
    permitido = False
    if atraccion == 1 and edad >= 12:
        permitido = True
    elif atraccion == 2:
        permitido = True
    elif atraccion == 3 and edad >= 15:
        permitido = True
    
    return permitido

#Precio
def calcular_precio(atraccion):
    precio = 0
    if atraccion == 1:
        precio = 1500
    elif atraccion == 2:
        precio = 800
    elif atraccion == 3:
        precio = 1200

    return precio

#Registro de visita
def registrar_visita():
    nombre = input("Ingrese el nombre del visitante: ")
    edad = int(input("Ingrese la edad: "))

    total = 0
    cantidad = 0
    seguir = "s"

    while seguir == "s":
        mostrar_atracciones()
        seleccion = int(input("Seleccione la atracción (número): "))
        
        if puede_subir(edad, seleccion):
            precio = calcular_precio(seleccion)
            total += precio
            cantidad += 1
            atraccion = seleccion
            print("Atracción agregada. Precio:", precio)
        else:
            atraccion = "No puede entrar"
            print("No puede entrar a esa atracción.")
        
        seguir = input("¿Desea agregar otra atracción? (s/n): ")

    #Descuentos
    if cantidad >= 3:
        descuento = total * 0.10
        total -= descuento
        print("Se aplicó un descuento del 10%.")

    return nombre, edad, cantidad, total

#Resumen
def mostrar_resumen(nombre, edad, atraccion, precio):
    print("---Resumen de la visita---")
    print("Nombre:", nombre)
    print("Edad:", edad)
    print("Atracciones elegidas:", atraccion)
    print("Costo total:", precio)
    print("--------------------------")
