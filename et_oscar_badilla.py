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
    
def busqueda_precio(precio_min, precio_max, hechizos, reservas):
    hechizos_en_rango = []
    
    for codigo, datos in hechizos.items():
        precio, stock = reservas[codigo]
        if precio_min <= precio <= precio_max and stock > 0:
            hechizos_en_rango.append(f"{datos[0]}--{codigo}")
    
    if hechizos_en_rango:
        hechizos_en_rango.sort()
        print("Hechizos disponibles en el rango de precios:")
        for hechizo in hechizos_en_rango:
            print(hechizo)
    else:
        print("No hay hechizos en ese rango de precios.")

def buscar_codigo(codigo):
    return codigo.upper() in reservas

def actualizar_precio(codigo, nuevo_precio, reservas):
    if buscar_codigo(codigo):
        reservas[codigo] = [nuevo_precio, reservas[codigo][1]]
        return True
    return False

def validar_codigo(codigo):
    return codigo.strip() != "" and not buscar_codigo(codigo)

def validar_nombre(nombre):
    return nombre.strip() != ""

def validar_escuela(escuela):
    return escuela.lower() in ['elemental', 'arcana', 'oscura']

def valida_mayor_cero(valor):
    try:
        valor = int(valor)
        return valor > 0
    except ValueError:
        return False
    
def validar_poder(poder):
    return valida_mayor_cero(poder)

def validar_rareza(rareza):
    return rareza.upper() in ['C', 'R', 'L']

def validar_es_prohibido(es_prohibido):
    return es_prohibido.lower() in ['s', 'n']

def validar_creador(creador):
    return creador.strip() != ""

def validar_precio(precio):
    return valida_mayor_cero(precio)

def validar_stock(stock):
    try:
        stock = int(stock)
        return stock >= 0
    except ValueError:
        return False

def agregar_hechizo(codigo, nombre, escuela, poder, rareza, es_prohibido, creador, precio, stock, hechizos, reservas):
    if buscar_codigo(codigo):
        return False
    hechizos[codigo] = [nombre, escuela, poder, rareza, es_prohibido, creador]
    reservas[codigo] = [precio, stock]
    return True

def eliminar_hechizo(codigo, hechizos, reservas):
    if buscar_codigo(codigo):
        del hechizos[codigo]
        del reservas[codigo]
        return True
    return False

while True:
    opcion = leer_opcion()
    
    if opcion == 1:
        escuela = input("Ingrese la escuela de magia: ")
        pergaminos_escuela(escuela, hechizos, reservas)
    elif opcion == 2:
        # Implementar búsqueda de hechizos por rango de precio
        while True:
            try:
                precio_min = int(input("Ingrese el precio mínimo: "))
                precio_max = int(input("Ingrese el precio máximo: "))
                if precio_min < 0 or precio_max < 0 or precio_min > precio_max:
                    print("Debe ingresar valores válidos para el rango de precios.")
                else:
                    busqueda_precio(precio_min, precio_max, hechizos, reservas)
                    break
            except ValueError:
                print("Debe ingresar valores enteros.") 
    elif opcion == 3:
        # Implementar actualización de precio de hechizo
        while True:
            try:
                codigo = input("Ingrese el código del hechizo: ")
                if not buscar_codigo(codigo):
                    print("El código no existe.")
                else:
                    nuevo_precio = int(input("Ingrese el nuevo precio: "))
                    if nuevo_precio < 0:
                        print("El precio debe ser un valor positivo.")
                    else:
                        if actualizar_precio(codigo, nuevo_precio, reservas):
                            print("Precio actualizado.")
                        else:
                            print("El código no existe")
                respuesta = input("¿Desea actualizar otro precio (s/n)? ")
                if respuesta.lower() == "n":
                    break
            except ValueError:
                print("Debe ingresar un valor entero para el precio.")
    elif opcion == 4:
        # Implementar agregar hechizo
        codigo = input("Ingrese el código del hechizo: ")
        
        if not validar_codigo(codigo):
            print("Código inválido o ya existe.")
            continue
        nombre = input("Ingrese el nombre del hechizo: ")
        if not validar_nombre(nombre):
            print("Nombre inválido.")
            continue
        escuela = input("Ingrese la escuela de magia: ")
        if not validar_escuela(escuela):
            print("Escuela inválida.")
            continue
        poder = input("Ingrese el poder del hechizo: ")
        if not validar_poder(poder):
            print("Poder inválido.")
            continue
        rareza = input("Ingrese la rareza del hechizo (C, R, L): ")
        if not validar_rareza(rareza):
            print("Rareza inválida.")
            continue
        es_prohibido = input("¿Es prohibido? (s/n): ")
        if not validar_es_prohibido(es_prohibido):
            print("Valor inválido para es_prohibido.")
            continue
        creador = input("Ingrese el nombre del creador: ")
        if not validar_creador(creador):
            print("Creador inválido.")
            continue
        precio = input("Ingrese el precio del hechizo: ")
        if not validar_precio(precio):
            print("Precio inválido.")
            continue
        stock = input("Ingrese el stock disponible: ")
        if not validar_stock(stock):
            print("Stock inválido.")
            continue
        #Agregamos el hechizo
        if agregar_hechizo(codigo, nombre, escuela, int(poder), rareza.upper(), es_prohibido.lower() == 's', creador, int(precio), int(stock), hechizos, reservas):
            print("Hechizo agregado.")
        else:
            print("El código ya existe.")
    elif opcion == 5:
        # Implementar eliminar hechizo
        codigo = input("Ingrese el código del hechizo a eliminar: ")
        if eliminar_hechizo(codigo, hechizos, reservas):
            print("Hechizo eliminado.")
        else:
            print("El código no existe.")
    elif opcion == 6:
        print("Saliendo del programa...")
        break