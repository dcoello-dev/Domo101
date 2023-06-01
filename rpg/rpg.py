# Alcance

# 1-> Almacene informacion del jugador (nombre)
# 2-> Gestione el personaje del jugador (nombre)
# 3-> Tiradas de dados

# Conceptos

# Jugador (nombre, estadisitcas?, personaje)
# Personaje (nombre)

import json
import random

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
ROJO = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


def guardar_jugador(jugador):
    """guarda la jugador en un fichero"""
    # escribir en un archivo

    # w: para escribir en el
    # r: para leer
    # +: para crearlo si no existe
    archivo = open("./bd.json", "w+")

    # pasamos la jugador a un string en formato json
    jugador_en_json = json.dumps(jugador, indent=2)

    # lo enchuflamos al archivo
    archivo.write(jugador_en_json)

    # cerramos archivo
    archivo.close()


def cargar_jugador():
    """cargar la jugador desde un fichero"""
    try:
        archivo = open("bd.json", "r")

        # leemos el archivo
        jugador_en_json = archivo.read()

        # pasar el string a un array
        jugador = json.loads(jugador_en_json)

        # cerramos el archivo
        archivo.close()

    except FileNotFoundError:
        print("No se ha encontrado bd.json, creando nuevo jugador")
        # si no existe el archivo con los datos pedimos el jugador al usuario
        jugador = nuevo_jugador()

        # una vez nos lo da lo guardamos en el archivo para la siguiente vez
        guardar_jugador(jugador)
        return jugador

    # retornamos el array de la jugador
    return jugador


def nuevo_jugador():
    """pedir datos al jugador"""
    nombre_usuario = input("tu nombre: ")
    nombre_personaje = input("nombre de tu personaje: ")
    personaje = dict(nombre=nombre_personaje, vida=100)
    jugador = dict(
        nombre=nombre_usuario,
        estadisticas=dict(),
        personaje=personaje)
    return jugador


def tirada():
    return random.randint(1, 20)


def colorear(color, mensaje):
    return f"{color}{mensaje}{ENDC}"


def mostrar_jugador(jugador):
    nombre = jugador['nombre'].capitalize()
    personaje = jugador['personaje']['nombre']
    vida = jugador['personaje']['vida']

    color = ROJO
    if vida >= 70:
        color = OKGREEN
    elif vida >= 30:
        color = WARNING

    print(f"{nombre}\n\t{personaje}({colorear(color, vida)})")


def mostrar_tirada(tirada):
    color = OKBLUE
    if tirada == 20:
        color = OKGREEN
    elif tirada == 1:
        color = ROJO
    print(f"Tirada: {colorear(color, tirada)}")


def bucle_de_eventos(jugador):
    decision = ""
    while decision != "q":
        decision = input(
            "Accion \n\t(q/salir) \n\t(r/tirar) \n\t(m/mostrar)\n-> ")
        if decision == "r":
            resultado = tirada()
            mostrar_tirada(resultado)
            jugador['personaje']['vida'] = jugador['personaje']['vida'] - resultado

        elif decision == "m":
            mostrar_jugador(jugador)

        if jugador['personaje']['vida'] < 0:
            print("TE MORISTE")
            return


jugador = cargar_jugador()

bucle_de_eventos(jugador)
