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
