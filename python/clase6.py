# 1 se le pasa una o multiple informacion
# 2 realiza una, ninguna o multiples acciones
# 3 devuelve algo o nada

# quierop una funcion que dada una lista me saque por pantalla la lista y
# su longitud

# lista(longitud): [basjdbasdjk]

def mostrar_lista(lista_de_entrada):
    print("lista(" + str(len(lista_de_entrada)) + ")")

    indice = 0
    for elem in lista_de_entrada:
        print(str(indice) + ": " + str(elem))
        indice = indice + 1


def multiplicar(n0, n1):
    acumulado = 0
    for vez in range(0, n0):
        acumulado = acumulado + n1
        print("vez: " + str(vez) + " " + str(acumulado))
    return acumulado

# ffuncion que dado un array de numeros me devuelve el numero de 4


def cuenta_cuatros(array):
    contador = 0
    for num in array:
        if num == 4:
            contador = contador + 1
    return contador


def donde_cuatro(array):
    posicion = 0
    for num in array:
        if num == 4:
            return posicion
        posicion = posicion + 1
    return -1


def acumulado(array):
    suma = 0
    for num in array:
        suma = suma + num
    return suma


def acumulado_indices(array):
    suma = 0
    indice = 0
    for _ in array:
        suma = suma + indice
        indice = indice + 1
    return suma


clase = ["acenha", "diego", "martin"]

otra_lista = [4, 5, 3, 4]

# mostrar_lista(clase)
mostrar_lista(otra_lista)
longitud = 0
resultado = multiplicar(3, 3)
print("multiplicacion: " + str(resultado))
print("cuenta_cuatros: " + str(cuenta_cuatros(otra_lista)))
print("donde_cuatro: " + str(donde_cuatro(otra_lista)))
print("acumulado: " + str(acumulado(otra_lista)))
print("acumulado_indices: " + str(acumulado_indices(otra_lista)))

# print(longitud)
