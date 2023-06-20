# - mew
# - mirar con desprecio
# - come
# - juega

# - datos -> parte estatica
# - comportamieto -> parte dinamica

class Gato:
    def __init__(self,
                nombre_de_entrada,
                color_de_entrada):
        self.nombre = nombre_de_entrada
        self.color = color_de_entrada
        self.mostrar()

    def mostrar(self):
        print(self.color.colorear(f"Gato {self.nombre}"))

    def hablar(self):
        print(self.color.colorear("mew!"))

    def comer(self):
        print(self.color.colorear("ñom!"))

