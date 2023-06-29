import time
import json
import random

from DMKernel.Component import Component

# 1-> heredar de componente
# 2-> pasarle conf con los campos adecuados al constructor de componente
# 3-> implementar el metodo proc
# 4-> no olvidarse de hacer el start()

class Controller(Component):
    def __init__(self, conf, id):
        super().__init__(conf)
        self._id = id

    def proc(self, msg):
        print(f"recibido -> {msg['payload']}")

    def publish_msg(self, topic, msg):
        self.iface_.on_publish(topic, json.dumps(dict(msg=msg, id=self._id)))

with open("conf.json", "r")as conf_file:
    CONF = json.loads(conf_file.read())

print(CONF)
cont = Controller(CONF, random.randint(0,10))
cont.start()

while True:
    mensaje = input("mensaje: ")
    cont.publish_msg("/Domo101/prueba", mensaje)
    time.sleep(0.1)

