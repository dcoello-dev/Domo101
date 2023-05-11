numero_entero = 1
numeros_flotantes = 1.0
variable_booleana = False
variable_string = "hola soy"
variable_caracter = 'a'
variable = None

print(numero_entero)
print(numeros_flotantes)
print(variable_booleana)
print(variable_string)
print(variable_caracter)
print(variable)

var = numero_entero
print(var)
var = variable_string
print(var)

print(numero_entero + numeros_flotantes)
print(int(numeros_flotantes + numero_entero))
print(variable_string + str(numero_entero))

name = "david"
print("hola " + name)
print(variable_booleana + numero_entero)
print(str(variable_booleana))

print(str(type(variable_booleana).__name__))
for elem in vv:
    if elem == 2:
        print("este es el 2")
    elif type(elem) == float:
        print("este es el raro")
    else:
        print(elem)

array = []
print(array)
print(len(array))

array.append(1)
print(array)
print(len(array))
array.append(2)
print(array)
print(len(array))
array.append(3)
print(array)
print(len(array))

array.append(True)
print(array)
print(len(array))

array.append(7.8)
print(array)
print(len(array))

array.append(type(7.8))
print(array)
print(len(array))

print(array[2])
array[2] = 6
print(array)

array.reverse()

vv = [1, 2, 3, "5", 4, 6]

for elem in vv:
    print(elem)

flag = True
if flag:
    print("me ejecuto")



alumnos = ["alex", "bene", "martin", "nacho"]

alumnos.append("acenha")

alumnos.sort()

alumnos.reverse()

print(alumnos)

# 1: recorrer array
for indice, alumno in enumerate(alumnos):
    # 2: asignar nuevo nombre a cada alumno
    print(str(indice) + " " + alumno)
    alumnos[indice] = "alumno: " + alumno

for i in range(0, len(alumnos)):
    alumnos[i] = "alumno: " + alumnos[i]

print(alumnos)
