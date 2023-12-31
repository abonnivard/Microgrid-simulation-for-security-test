from pyModbusTCP.server import ModbusServer, DataBank
from time import sleep
# Configuration du serveur Modbus
MODBUS_SERVER_HOST = '192.168.64.4'  # Adresse IP du serveur Modbus
MODBUS_SERVER_PORT = 502      # Port par défaut pour Modbus TCP

# Création du serveur Modbus
server = ModbusServer(host=MODBUS_SERVER_HOST, port=MODBUS_SERVER_PORT)
db = server.data_bank
server.start()


while True:
    sleep(0.5)
    


