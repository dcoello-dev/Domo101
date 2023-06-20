import time

from src.Gato import Gato
from src.Color import *
from src.Tienda import *

print("Tienda Gatitos")

maquiavelo = Gato("maquiavelo", Color(Color.VERDE))
blanquito = Gato("blanquito", Color(Color.BOLD))
salmoncete = Gato("salmoncete", Color(Color.NARANJA))

mi_tienda = Tienda(5)

mi_tienda.nuevo_gatito(maquiavelo)
mi_tienda.nuevo_gatito(blanquito)
mi_tienda.nuevo_gatito(salmoncete)

while(True):
    time.sleep(1)
    mi_tienda.llenar_comederos()

# comedero1.llenar()
# time.sleep(1)
# comedero1.llenar()

# mi_tienda = Tienda(2)
# # maquiavelo.mostrar()
