import time
import json
import argparse
import telepot

from DMKernel.Component import Component

class Controller(Component):
    def __init__(self, conf):
        super().__init__(conf)
        self.conf = conf

    def proc(self, msg):
        print(f"Estado: {msg['payload']['estado']}")

    def publish_msg(self, comando, duracion):
        self.iface_.on_publish(self.conf["component_conf"]["publicar"],
                                json.dumps(dict(comando=comando, duracion=duracion)))

class TUIinterfaz:
    def __init__(self, controlador):
        self.controlador = controlador

    def interfacear(self):
        while True:
            cc = input ("comando: ")
            self.controlador.publish_msg(cc, 0)
            time.sleep(0.1)

class TelegraInterfaz:
    def __init__(self, controlador, bot):
        self.bot = bot
        print(json.dumps(self.bot.getMe(), indent=2))
        self.controlador = controlador

    def interfacear(self):
        update_id = 0
        while True:
            time.sleep(1)
            msg = self.bot.getUpdates(offset=update_id)
            if len(msg) > 0:
                for m in msg:
                    print(m)
                    self.controlador.publish_msg(m['message']['text'], 0)
                    print(f"comando {m['message']['text']}")
                update_id = msg[-1]["update_id"] + 1

class CLIinterfaz:
    def __init__(self, controlador, args):
        self.controlador = controlador
        self.args = args

    def interfacear(self):
        self.controlador.publish_msg(args.cmd, 0)
        time.sleep(1)
        self.controlador.stop()

parser = argparse.ArgumentParser()

parser.add_argument(
    '-m', '--mode',
    default='tui',
    help="modo interfaz")

parser.add_argument(
    '-c', '--cmd',
    default='comprobar',
    help="comando")

args = parser.parse_args()

with open("cc_conf.json", "r")as conf_file:
    CONF = json.loads(conf_file.read())

print(CONF)
bot = None
if args.mode == "tele":
    bot = telepot.Bot('TOKENBOT')

cont = Controller(CONF)
if args.mode == "tui":
    iface = TUIinterfaz(cont)
elif args.mode == "cli":
    iface = CLIinterfaz(cont, args)
else:
    iface = TelegraInterfaz(cont, bot)

cont.start()

iface.interfacear()

