import socket
import json
import struct
import numpy as np
from pyModbusTCP.client import ModbusClient
from time import sleep


#ouverture du client modbus
client= ModbusClient(host="192.168.64.4", port=502)
client.open()

#ouverture du client TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1',9999))
s.listen(5)
print('waiting for connection...')
sock, addr = s.accept()

print('Initialisation')
#Initialisation du server modbus
buf = sock.recv(1000)
buf_1 = buf
buf_2 = struct.unpack('ddddd', buf_1[0:40])
tension1 = buf_2[3]
intensite1 = buf_2[4]
boutton1 = buf_2[0]
boutton2 = buf_2[1]
boutton3 = buf_2[2]


client.write_single_coil(0,boutton1)
client.write_single_coil(1,boutton2)
client.write_single_coil(2,boutton3)
client.write_single_register(0, int(tension1))
client.write_single_register(1, int(intensite1))

control_signal4 = tension1
control_signal5 = intensite1
control_signal1 = (client.read_coils(0, bit_nb=1))[0]
control_signal2 = (client.read_coils(1, bit_nb=1))[0]
control_signal3 = (client.read_coils(2, bit_nb=1))[0]
control_signal = np.array([control_signal1, control_signal2, control_signal3, control_signal4, control_signal5], int )
s = str(control_signal)
s_l = bytes(s, encoding='utf8')
sock.send(s_l)
print(s)

try:
    while True:
        sleep(0.5)
        buf = sock.recv(1000)
        buf_1 = buf
        buf_2 = struct.unpack('ddddd', buf_1[0:40])
        tension1 = buf_2[3]
        intensite1 = buf_2[4]
        boutton1 = buf_2[0]
        boutton2 = buf_2[1]
        boutton3 = buf_2[2]
        print(buf_2)

        #Mise a jour des valeurs
        client.write_single_register(0, int(tension1))
        client.write_single_register(1, int(intensite1))

        control_signal4 = tension1
        control_signal5 = intensite1
        control_signal1 = (client.read_coils(0, bit_nb=1))[0]
        control_signal2 = (client.read_coils(1, bit_nb=1))[0]
        control_signal3 = (client.read_coils(2, bit_nb=1))[0]
        control_signal = np.array([control_signal1, control_signal2, control_signal3, control_signal4, control_signal5], int)
        s = str(control_signal)
        s_l = bytes(s, encoding='utf8')
        sock.send(s_l)
        print(s)

except KeyboardInterrupt:
    # Fermer la socket lorsque le bloc try est terminé ou si une exception est levée
    sock.close()
