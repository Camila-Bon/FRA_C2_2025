# 1-----------------------------------------------------------
FILAS = 7  #días
COLUMNAS = 3  #horarios
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
horarios = ["Mañana", "Tarde", "Noche"]

def cargar_temperaturas(mat):
    print("Cargar temperaturas")
    for i in range(FILAS):
        print(f"Día: {dias[i]}")
        for j in range(COLUMNAS):
            valor_valido = False
            while valor_valido == False:
                temp = int(input(f"Ingrese temperatura ({horarios[j]}): "))
                mat[i][j] = temp
                valor_valido = True

def mostrar_promedios(mat):
    acumulador_total = 0
    for i in range(FILAS):
        acumulador_dia = 0
        for j in range(COLUMNAS):
            acumulador_dia += mat[i][j]
        promedio_dia = acumulador_dia / COLUMNAS
        print(f"{dias[i]} - Promedio: {promedio_dia:.2f}")
        acumulador_total += acumulador_dia
    promedio_general = acumulador_total / (FILAS * COLUMNAS)
    print(f"Promedio general de la semana: {promedio_general:.2f}")

temperaturas = [[0]*COLUMNAS for _ in range(FILAS)]

cargar_temperaturas(temperaturas)
mostrar_promedios(temperaturas)

#2-----------------------------------------------------------
EQUIPOS = 4
RONDAS = 5

def cargar_puntajes(mat):
    print("Cargar puntajes")
    for i in range(EQUIPOS):
        print(f"Equipo {i + 1}")
        for j in range(RONDAS):
            valor_valido = False
            while valor_valido == False:
                puntaje = int(input(f"Ingrese puntaje ronda {j+1}: "))
                if puntaje >= 0:
                    mat[i][j] = puntaje
                    valor_valido = True
                else:
                    print("No se permiten negativos")

def mostrar_totales(mat):
    acumuladores = [0]*EQUIPOS
    for i in range(EQUIPOS):
        for j in range(RONDAS):
            acumuladores[i] += mat[i][j]
        print(f"Equipo {i+1} - Puntaje total: {acumuladores[i]}")

    mayor = acumuladores[0]
    equipo_ganador = 1
    for i in range(1, EQUIPOS):
        if acumuladores[i] > mayor:
            mayor = acumuladores[i]
            equipo_ganador = i + 1
    print(f"Equipo con mayor puntaje: Equipo {equipo_ganador} ({mayor} puntos)")

puntajes = [[0]*RONDAS for _ in range(EQUIPOS)]

cargar_puntajes(puntajes)
mostrar_totales(puntajes)

#3-----------------------------------------------------------
PRODUCTOS = 3
DIAS = 4

def cargar_produccion(mat):
    print("Cargar producción")
    for i in range(PRODUCTOS):
        print(f"Producto {i + 1}")
        for j in range(DIAS):
            valor_valido = False
            while valor_valido == False:
                cantidad = int(input(f"Cantidad producida día {j+1}: "))
                if cantidad >= 0:
                    mat[i][j] = cantidad
                    valor_valido = True
                else:
                    print("No se permiten negativos")

def mostrar_produccion(mat):
    for i in range(PRODUCTOS):
        acumulador_producto = 0
        for j in range(DIAS):
            acumulador_producto += mat[i][j]
        print(f"Producto {i+1} - Producción total: {acumulador_producto}")

    for j in range(DIAS):
        acumulador_dia = 0
        for i in range(PRODUCTOS):
            acumulador_dia += mat[i][j]
        print(f"Día {j+1} - Producción total: {acumulador_dia}")

    totales_dias = [0]*DIAS
    for j in range(DIAS):
        for i in range(PRODUCTOS):
            totales_dias[j] += mat[i][j]

    mayor = totales_dias[0]
    dia_mayor = 1
    for j in range(1, DIAS):
        if totales_dias[j] > mayor:
            mayor = totales_dias[j]
            dia_mayor = j + 1

    print(f"Día con mayor producción: Día {dia_mayor} ({mayor} unidades)")

produccion = [[0]*DIAS for _ in range(PRODUCTOS)]

cargar_produccion(produccion)
mostrar_produccion(produccion)