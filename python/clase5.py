
# # vector o array
# array = [1, 2, 3]
# print_list(array)

# array.append(4)
# print_list(array)

# # del 0 al len() - 1
# array[0] = 9
# print_list(array)

# array.sort()
# print_list(array)

# array.reverse()
# print_list(array)


def rango(desde, hasta):
    array = []
    while desde < hasta:
        array.append(desde)
        desde = desde + 1
    return array

def print_list(lista):
    print("lista: " + str(len(lista)))

    for i in rango(0, len(lista)):
        print(str(i) + ": " + lista[i])

    print()

def saludo(nombre):
    print("hola, " + str(nombre))


clase = ["nacho", "david", "jorge"]
clase.sort()
clase.append("alex")
clase.sort()
# print(clase[1])
print_list(clase)

# for alumno in clase:
#     if alumno == "jorge":
#         print("bienvenido")
#     else:
#         saludo(alumno)

# print(list(range(0, 5)))



# for alumno in clase:
#     print(alumno)
# for num_alumno in range(0, len(clase)):
#     print(num_alumno)


# print(rango(1, 7))

def acumulado(valores):
    acum = 0
    for valor in valores:
        acum = acum + valor
    return acum

vector = [1, 2, 3, 4, 2, 1]

print(acumulado(vector))

