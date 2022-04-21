from os import chdir, system as sysos
from colorama import Fore
from time import sleep
from platform import uname
# Cut
try:
    def SystemClear(system):
        system = uname()[0]
        if system == 'Linux':
            sysos('clear')
        else:
            sysos('cls')
            print(Fore.LIGHTRED_EX+'Script Not Run in Windows')

    SystemClear(system=sysos)
    # Cut
    sleep(1)
    print(Fore.LIGHTBLACK_EX+'''
    ███████████                      █████
    ░░███░░░░░███                    ░░███
    ░███    ░███  ██████  █████ ████ ░███████   ██████  ████████
    ░██████████  ███░░███░░███ ░███  ░███░░███ ███░░███░░███░░███
    ░███░░░░░░  ░███ ░░░  ░███ ░███  ░███ ░███░███████  ░███ ░░░
    ░███        ░███  ███ ░███ ░███  ░███ ░███░███░░░   ░███
    █████       ░░██████  ░░███████  ████████ ░░██████  █████
    ░░░░░         ░░░░░░    ░░░░░███ ░░░░░░░░   ░░░░░░  ░░░░░
                            ███ ░███
                        ░░██████
                            ░░░░░░
    ''')
    # Cut
    def List():
        sleep(0.45)
        print(Fore.RED+'['+Fore.WHITE+'1'+Fore.RED+']'+Fore.LIGHTCYAN_EX+' ⟹'+Fore.WHITE+' Creator'+Fore.RED+' Ngrok'+Fore.WHITE+' Tcp'+Fore.YELLOW+' !\n')
        sleep(0.25)
        print(Fore.RED+'['+Fore.WHITE+'2'+Fore.RED+']'+Fore.LIGHTCYAN_EX+' ⟹'+Fore.WHITE+' Run in'+Fore.RED+' Localhost'+Fore.YELLOW+' !\n')
        sleep(0.25)
        print(Fore.RED+'['+Fore.WHITE+'3'+Fore.RED+']'+Fore.LIGHTCYAN_EX+' ⟹'+Fore.WHITE+' Creator'+Fore.LIGHTGREEN_EX+' Paylaod'+Fore.RED+' *\n')
        sleep(0.5)
        print(Fore.RED+'['+Fore.WHITE+'99'+Fore.RED+']'+Fore.LIGHTCYAN_EX+' ⟹'+Fore.WHITE+' Info '+Fore.RED+'Localhost'+Fore.LIGHTYELLOW_EX+' / '+Fore.RED+'Ngrok'+Fore.GREEN+' ?\n\n')
    List()
    # Cut
    def Selects():
        selects = int(input(Fore.RED+'┌─['+Fore.GREEN+'PayloadCyber'+Fore.YELLOW+'~'+Fore.LIGHTYELLOW_EX+'HOST'+Fore.RED+Fore.RED+']'+'\n└──╼> '+Fore.WHITE))
        if selects == 1:
            sysos('python3 Ngrok.py')
        elif selects == 2:
            sysos('python3 exploit.py')
        elif selects == 3:
            sysos('python3 exploit.py')
        elif selects == 99:
            chdir('Info')
            sysos('ruby info.rb')
        elif selects >= 0:
            sysos('python3 payloads.py')
    Selects()
except KeyboardInterrupt:
    print('Good bye :)')
except ValueError:
    print(Fore.RED+'Value Error :|')