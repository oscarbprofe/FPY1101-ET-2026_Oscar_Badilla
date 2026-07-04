'''
La Academia de Hechicería Astralis requiere un programa en Python para administrar su
grimorio de hechizos
'''

# Hechizos: nombre, escuela, poder, rareza, es_prohibido, creador.
hechizos = {
 'H001': ['Llamarada Solar', 'elemental', 5, 'C', False, 'Ignus el Ardiente'],
 'H002': ['Escudo de Escarcha', 'elemental', 3, 'C', False, 'Dama Fenwick'],
 'H003': ['Rayo Astral', 'arcana', 7, 'R', False, 'Magíster Orin'],
 'H004': ['Cadena de Almas', 'oscura', 9, 'L', True, 'El Innombrable'],
 'H005': ['Portal Menor', 'arcana', 4, 'R', False, 'Selene Valdour'],
 'H006': ['Toque Vampírico', 'oscura', 6, 'R', True, 'Mordath'],
}

#Reserva: precio (cristales de maná), stock (cantidad de pergaminos disponibles)
reservas = {
 'H001': [120, 8],
 'H002': [90, 0],
 'H003': [340, 3],
 'H004': [999, 2],
 'H005': [210, 5],
 'H006': [450, 4],
}

def leer_opcion():

    print('''
    ========= GRIMORIO ASTRALIS =========
    1. Pergaminos por escuela de magia
    2. Búsqueda de hechizos por rango de precio
    3. Actualizar precio de hechizo
    4. Agregar hechizo
    5. Eliminar hechizo
    6. Salir
    =====================================
    ''')
    try:
        eleccion = int(input("Ingrese una opción: "))
        if eleccion < 1 or eleccion > 6:
            print("Debe seleccionar una opción válida")
            return 0
        return eleccion
    except ValueError:
        print("Debe seleccionar una opción válida")
        return 0

def pergaminos_escuela(escuela, hechizos, reservas):
    print(f"Pergaminos disponibles para la escuela de magia '{escuela}':")
    cont_pergaminos_escuela = 0
    
    for codigo, datos in hechizos.items():
        if datos[1].lower() == escuela.lower():
            cont_pergaminos_escuela += reservas[codigo][1]
    
    print(f"Total de pergaminos para la escuela '{escuela}': {cont_pergaminos_escuela}")
    

while True:
    opcion = leer_opcion()
    
    if opcion == 1:
        escuela = input("Ingrese la escuela de magia: ")
        pergaminos_escuela(escuela, hechizos, reservas)
    elif opcion == 2:
        # Implementar búsqueda de hechizos por rango de precio
        pass
    elif opcion == 3:
        # Implementar actualización de precio de hechizo
        pass
    elif opcion == 4:
        # Implementar agregar hechizo
        pass
    elif opcion == 5:
        # Implementar eliminar hechizo
        pass
    elif opcion == 6:
        print("Saliendo del programa...")
        break