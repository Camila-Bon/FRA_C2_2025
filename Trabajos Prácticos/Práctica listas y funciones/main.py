#listas estáticas (máx. 20 libros).-
titulos = [""] * 20
ejemplares = [0] * 20
cantidad = 0  #cantidad de libros cargados..-

# 1-
def cargar_titulos(titulos, ejemplares, cantidad):
    while cantidad < 20:
        titulo = input("Ingrese título (o ENTER para terminar): ")
        if titulo == "":
            break
        copias = int(input("Cantidad de ejemplares: "))
        titulos[cantidad] = titulo
        ejemplares[cantidad] = copias
        cantidad += 1
    return cantidad

# 2-
def mostrar_catalogo(titulos, ejemplares, cantidad):
    print("--- Catálogo ---")
    for i in range(cantidad):
        print(titulos[i], ":", ejemplares[i], "copias")

# 3-
def consultar_disponibilidad(titulos, ejemplares, cantidad):
    titulo = input("Ingrese el título a consultar: ")
    encontrado = False
    for i in range(cantidad):
        if titulos[i] == titulo:
            print(titulo, ":", ejemplares[i], "copias")
            encontrado = True
    if not encontrado:
        print("El título no se encuentra en el catálogo.")

# 4-
def listar_agotados(titulos, ejemplares, cantidad):
    print("--- Títulos agotados ---")
    hay_agotados = False
    for i in range(cantidad):
        if ejemplares[i] == 0:
            print(titulos[i])
            hay_agotados = True
    if not hay_agotados:
        print("Ningún título está agotado.")

# 5-
def agregar_titulo(titulos, ejemplares, cantidad):
    if cantidad >= 20:
        print("No se pueden agregar más títulos (máx. 20).")
    else:
        titulo = input("Ingrese nuevo título: ")
        copias = int(input("Cantidad de ejemplares: "))
        titulos[cantidad] = titulo
        ejemplares[cantidad] = copias
        cantidad += 1
        print("Título agregado correctamente.")
    return cantidad

# 6-
def actualizar_ejemplares(titulos, ejemplares, cantidad):
    titulo = input("Ingrese el título a actualizar: ")
    encontrado = False
    for i in range(cantidad):
        if titulos[i] == titulo:
            cambio = int(input("Ingrese cantidad (+ devolución, - préstamo): "))
            ejemplares[i] += cambio
            if ejemplares[i] < 0:
                ejemplares[i] = 0
            print("Ejemplares de", titulo, "actualizados a", ejemplares[i])
            encontrado = True
    if not encontrado:
        print("El título no existe.")

#menú
while True:
    print("--- Menú Biblioteca ---")
    print("1. Cargar títulos y ejemplares")
    print("2. Mostrar catálogo completo")
    print("3. Consultar disponibilidad")
    print("4. Listas de títulos agotados")
    print("5. Agregar nuevo título")
    print("6. Actualizar ejemplares (préstamo/devolución)")
    print("7. Salir")
    
    opcion = input("Elija una opción: ")
    
    if opcion == "1":
        cantidad = cargar_titulos(titulos, ejemplares, cantidad)
    elif opcion == "2":
        mostrar_catalogo(titulos, ejemplares, cantidad)
    elif opcion == "3":
        consultar_disponibilidad(titulos, ejemplares, cantidad)
    elif opcion == "4":
        listar_agotados(titulos, ejemplares, cantidad)
    elif opcion == "5":
        cantidad = agregar_titulo(titulos, ejemplares, cantidad)
    elif opcion == "6":
        actualizar_ejemplares(titulos, ejemplares, cantidad)
    elif opcion == "7":
        print("Saliendo del sistema... Nos vemos!")
        break
    else:
        print("Opción inválida.")