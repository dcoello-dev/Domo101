import random

class Comedero:
    def __init__(self):
        self.gato = None
        self.lleno = False

    def asociar_gato(self, gato_asociado):
        self.gato = gato_asociado

    def asociado(self):
        return self.gato is not None

    def vacio(self):
        return not self.lleno

    def llenar(self):
        if self.lleno:
            print("Esta lleno!")
            return
        self.lleno = True
        if self.asociado():
            if (random.randint(1, 20) % 2 == 0):
                self.gato.comer()
                self.lleno = False

class Tienda:
    def __init__(self, numero_comederos):
        self.comederos = [Comedero() for _ in range(0, numero_comederos)]
        self.gatitos = []

    def nuevo_gatito(self, nuevo_gatito):
        nuevo_gatito.hablar()
        self.gatitos.append(nuevo_gatito)
        for comedero in self.comederos:
            if not comedero.asociado():
                comedero.asociar_gato(nuevo_gatito)
                comedero.llenar()
                nuevo_gatito.hablar()
                return

    def llenar_comederos(self):
        for comedero in self.comederos:
            if comedero.asociado() and comedero.vacio():
                print("comedero")
                comedero.llenar()


