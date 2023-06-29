import time
import json
from gpiozero import LED

from DMKernel.Component import Component

class ReleReal:
    def __init__(self):
        self.r = LED()

    def encender(self):
        self.r.on()

    def apagar(self):
        self.r.off()

    def comprobar(self):
        return " "


class ReleSimulado:
    def __init__(self):
        self.encendido = False

    def encender(self):
        if self.encendido:
            return "Rele: ya estaba encendido"
        else:
            self.encendido = True
            return "Rele: ENCENDIDO"

    def apagar(self):
        if not self.encendido:
            return "Rele: ya estaba apagado"
        else:
            self.encendido = False
            return "Rele: APAGADO"

    def comprobar(self):
        return f"Rele: {'ENCENDIDO' if self.encendido else 'APAGADO'}"

class Controller(Component):
    def __init__(self, conf):
        super().__init__(conf)
        self.conf = conf
        # try:
        #     self.rele = ReleReal()
        # except Exception as e:
        #     print("No gpiozero starting in simulated mode")
        self.rele = ReleSimulado()

    def proc(self, msg):
        if msg["payload"]["comando"] == "encender":
           self.publish_msg(self.rele.encender())
        if msg["payload"]["comando"] == "apagar":
           self.publish_msg(self.rele.apagar())
        if msg["payload"]["comando"] == "comprobar":
           self.publish_msg(self.rele.comprobar())

    def publish_msg(self, estado):
        self.iface_.on_publish(self.conf["component_conf"]["publicar"],
                                json.dumps(dict(estado=estado)))


with open("cr_conf.json", "r")as conf_file:
    CONF = json.loads(conf_file.read())

print(CONF)

cont = Controller(CONF)
cont.start()

while True:
    time.sleep(1)