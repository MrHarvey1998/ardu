import random
import os
import time
import sys
import serial
import serial.tools.list_ports
import configparser  # Importiere die configparser-Bibliothek

# Lade die Konfigurationsdatei
config = configparser.ConfigParser()
config.read('config.ini')

# Verwende die Werte aus der Konfigurationsdatei
bagheeracom = config['App']['com_port']

print("                    ")
print("    ──────▄▀▄─────▄▀▄")
print("    ─────▄█░░▀▀▀▀▀░░█▄")
print("    ─▄▄──█░░░░░░░░░░░█──▄▄")
print("    █▄▄█─█░░▀░░┬░░▀░░█─█▄▄█")
print("        Bagheera Aimbot")
print("                    ")
print("                    ")

# Keine Änderung in diesem Abschnitt des Codes erforderlich

class Mouse:    
    def __init__(self):
        self.serial_port = serial.Serial()
        self.serial_port.baudrate = 115200
        self.serial_port.timeout = 1
        self.serial_port.port = self.find_serial_port()
        try:
            self.serial_port.open()
        except serial.SerialException:
            sys.exit()

    def find_serial_port(self):
        port = next((port for port in serial.tools.list_ports.comports() if bagheeracom in port.description), None)
        if port is not None:
            return port.device
        else:
            sys.exit()

    def move(self, x, y):
        self.serial_port.write(f'MOVE{x},{y}\n'.encode('utf-8'))

    def close(self):
        self.serial_port.close()

    def __del__(self):
        self.close()
