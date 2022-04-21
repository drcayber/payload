from os import chdir , system as sys
from colorama import Fore
try:

    def BotTcp():
        port = int(input(Fore.RED+'\n┌─['+Fore.GREEN+'Port'+Fore.YELLOW+'~'+Fore.LIGHTYELLOW_EX+'Run'+Fore.RED+Fore.RED+']'+'\n└──╼> '+Fore.WHITE))
        data = chdir('Ngrok')
        sys('chmod +X *')
        sys('./ngrok tcp '+str(port))


    def BotHttp():
        port = int(input(Fore.RED+'\n┌─['+Fore.GREEN+'Port'+Fore.YELLOW+'~'+Fore.LIGHTYELLOW_EX+'Run'+Fore.RED+Fore.RED+']'+'\n└──╼> '+Fore.WHITE))
        data = chdir('Ngrok')
        sys('chmod +X *')
        sys('./ngrok http '+str(port))
except KeyboardInterrupt:
    print('Good bye :)')
except ValueError:
    print(Fore.RED+'Value Error :|')