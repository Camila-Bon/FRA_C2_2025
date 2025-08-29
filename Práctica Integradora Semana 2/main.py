from gestion_parque import parque

def main():
    nombre, edad, atraccion, precio = parque.registrar_visita()
    parque.mostrar_resumen(nombre, edad, atraccion, precio)

main()

