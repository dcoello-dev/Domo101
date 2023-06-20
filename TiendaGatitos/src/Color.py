class Color:
    MORAO = '\033[95m'
    AZUL = '\033[94m'
    CYAN = '\033[96m'
    VERDE = '\033[92m'
    NARANJA = '\033[93m'
    ROJO = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    SUB = '\033[4m'

    def __init__(self, color):
        self.color_interno = color

    def colorear(self, mensaje):
        return f"{self.color_interno}{mensaje}{self.ENDC}"
