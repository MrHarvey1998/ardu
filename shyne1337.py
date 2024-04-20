import cv2
import numpy as np
import threading
import time
import os
import win32api
import configparser  # Importiere die configparser-Bibliothek
import pyautogui

from screen_cap import ScreenCapture
from mouse import Mouse

# Lade die Konfigurationsdatei
config = configparser.ConfigParser()
config.read('config.ini')


LOWER_COLOR = np.array([140, 110, 150])
UPPER_COLOR = np.array([150, 195, 255])
THRESHOLD = 60

FOV = int(config['Settings']['fov'])
mvnt = float(config['Mouse']['mvnt'])
bone = int(config['Mouse']['bone'])
press_k = int(config['Settings']['press_k'], 16)
press_k2 = int(config['Settings']['press_k2'], 16)
trigger_k = int(config['Settings']['trigger_k'], 16)

speedx = float(config['Mouse']['speed'])
speedy = float(config['Mouse']['speed'])

class Shyne1337:
    def __init__(self, x, y, grabzone):
        self.arduinomouse = Mouse()
        self.grabber = ScreenCapture(x, y, grabzone)
        threading.Thread(target=self.run, daemon=True).start()
        self.toggled = False

    def toggle(self):
        self.toggled = not self.toggled
        time.sleep(0.2)

    def run(self):
        while True:
            if win32api.GetKeyState(press_k) < 0 and self.toggled:
                self.process("MOVE")
            elif win32api.GetKeyState(press_k2) < 0 and self.toggled:
                self.process("MOVE")
            elif win32api.GetKeyState(trigger_k) < 0 and self.toggled:
                self.process("press")
                
    def process(self, action):
        screen = self.grabber.get_screen()
        hsv = cv2.cvtColor(screen, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, LOWER_COLOR, UPPER_COLOR)
        dilated = cv2.dilate(mask, None, iterations=5)
        contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        if not contours:
            return

        contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(contour)
        center = (x + w // 2, y + h // 2)

        if action == "MOVE":
            cX = x + w // bone
            cY = y + 9
            x_diff = cX - self.grabber.grabzone // bone
            y_diff = cY - self.grabber.grabzone // bone
            self.arduinomouse.move(x_diff * speedx, y_diff * speedy)
            time.sleep(mvnt)
         
        if action == "press":
            cX = x + w // bone
            cY = y + 9
            x_diff = cX - self.grabber.grabzone // bone
            y_diff = cY - self.grabber.grabzone // bone
            pyautogui.click()
            
        

    def close(self):
        if hasattr(self, 'arduinomouse'):
            # Cleanup code for SocketArduinoMouse
            pass
        self.toggled = False

    def __del__(self):
        self.close()