import sys
import random


def mostrar_clase(clase):
    """mostrar la clase por pantalla"""
    num_alumno = 0
    for alumno in clase:
        num_alumno = num_alumno + 1
        # num_alumno: nombre_alumno
        # print(str(num_alumno) + ": " + alumno)
        print(f"{num_alumno}: {alumno.capitalize()}")


def capturar_entrada_usuario():
    """pedir nuevo alumno al ususario"""
    alumno = input("inserte nuevo alumno: ")
    print(f"Saludos {alumno}!")
    return alumno


def capturar_argumento():
    """comprobar argumentos"""
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        return "unknownsoldier"


def nuevo_alumno():
    """decidir de que manera se añade un nuevo alumno"""
    if len(sys.argv) > 1:
        return capturar_argumento()
    else:
        return capturar_entrada_usuario()


def esta_en_clase(alumno_entrada, clase):
    """comprobar si alumno esta en la clase"""
    for alumno in clase:
        if alumno == alumno_entrada:
            return True
    return False


def seleccionar_alumno_random(clase):
    indice_random = random.randint(0, len(clase) - 1)
    return clase[indice_random]


# definir
clase = ["acenha", "jorge", "alex"]

# nuevo alumno
n_a = nuevo_alumno()

# comprobar repetido
if not esta_en_clase(n_a, clase):
    # añadir
    clase.append(n_a)
else:
    print(f"{n_a.capitalize()} ya esta en clase")

# ordenar
clase.sort()

# mostrar
mostrar_clase(clase)

# seleccionar alumno random
print(f"Seleccionado: {seleccionar_alumno_random(clase).capitalize()}")
