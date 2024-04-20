import os
import time
import keyboard
from termcolor import colored
from shyne1337 import Shyne1337
import configparser

# Lade die Konfigurationsdatei
config = configparser.ConfigParser()
config.read('config.ini')

TOGGLE_KEY = 'F1'
press_k = int(config['Settings']['press_k'], 16)
mvnt = float(config['Mouse']['mvnt'])
bone = int(config['Mouse']['bone'])
speedx = float(config['Mouse']['speed'])
FOV = int(config['Settings']['fov'])
CENTER_X = int(config['Settings']['center_x'])
CENTER_Y = int(config['Settings']['center_y'])
CENTER_X, CENTER_Y = CENTER_X // 2, CENTER_Y // 2

def main():
    os.system('title MSI Afterburner')
    shyne1337_obj = Shyne1337(CENTER_X - FOV // 2, CENTER_Y - FOV // 2, FOV)
    print(colored(''' ''', 'yellow'))
    print()
    print(colored('[>]', 'red'), colored('Your Speed is', 'white'), colored (f'{speedx}', 'yellow'), colored (f'[<]', 'red'))
    print(colored('[>]', 'red'), colored('Your Bone is', 'white'), colored (f'{bone}', 'yellow'), colored (f'[<]', 'red'))
    print(colored('[>]', 'red'), colored('Your FOV is', 'white'), colored (f'{FOV}', 'yellow'), colored (f'[<]', 'red'))
    print(colored('[>]', 'red'), colored('Your mvnt is', 'white'), colored (f'{mvnt}', 'yellow'), colored (f'[<]', 'red'))
    print(colored('[>]', 'red'), colored('Set Enemies to', 'white'), colored('Purple', 'magenta'), colored (f'[<]', 'red'))
    print(colored('[>]', 'red'), colored(f'Press {TOGGLE_KEY} to toggle ON/OFF', 'white'), colored (f'[<]', 'red'))
    print()
    print(colored('[>]', 'red'), colored('Status', 'white'), colored('Undetected!', 'green'), colored (f'[<]', 'red'))
    print()
    print()
    status = 'Disabled'

    try:
        while True:
            if keyboard.is_pressed(TOGGLE_KEY):
                shyne1337_obj.toggle()
                status = (colored('Enabled', 'green')) if shyne1337_obj.toggled else (colored('Disabled', 'red'))
            print(f'\r{colored("[Status]", "green")} {colored(status, "white")}', end='')
            time.sleep(0.01)
    except (KeyboardInterrupt, SystemExit):
        print(colored('\n[Info]', 'blue'), colored('Exiting...', 'white') + '\n')
    finally:
        shyne1337_obj.close()

if __name__ == '__main__':
    main()
