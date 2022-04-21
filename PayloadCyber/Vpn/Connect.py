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
    Content = Fore.LIGHTCYAN_EX+'''
            _______  _        _______  _______  _        _        _______  _______ _________
    |\     /|(  ____ )( (    /|(  ____ \(  ___  )( (    /|( (    /|(  ____ \(  ____ \\__   __/
    | )   ( || (    )||  \  ( || (    \/| (   ) ||  \  ( ||  \  ( || (    \/| (    \/   ) (   
    | |   | || (____)||   \ | || |      | |   | ||   \ | ||   \ | || (__    | |         | |   
    ( (   ) )|  _____)| (\ \) || |      | |   | || (\ \) || (\ \) ||  __)   | |         | |   
    \ \_/ / | (      | | \   || |      | |   | || | \   || | \   || (      | |         | |   
    \   /  | )      | )  \  || (____/\| (___) || )  \  || )  \  || (____/\| (____/\   | |   
    \_/   |/       |/    )_)(_______/(_______)|/    )_)|/    )_)(_______/(_______/   )_(   
                                                                                            
    '''
    # Cut
    def mainConnect():
        SystemClear(system=sysos)
        print(Content)
        print(Fore.RED+'['+Fore.YELLOW+'!'+Fore.RED+'] '+Fore.WHITE+'Free vpn connection time\n')
        print(Fore.RED+'['+Fore.YELLOW+';'+Fore.RED+'] '+Fore.WHITE+'Download service-Ngrok in the new'+Fore.YELLOW+' Terminal\n')
        print(Fore.RED+'['+Fore.YELLOW+';'+Fore.RED+'] '+Fore.WHITE+'''Warning vpn will stop if you use the combination keys A and\n 
        Cvpn is connected through your shell system'''+Fore.YELLOW+' !\n')
        selects = str(input(Fore.RED+'┌─['+Fore.LIGHTGREEN_EX+' Connect'+Fore.YELLOW+' ~'+Fore.LIGHTYELLOW_EX+' Y / N '+Fore.RED+Fore.RED+']'+'\n└──╼> '+Fore.WHITE).casefold())
        sleep(1)
        if selects == 'y':
            pass
        else:
            chdir('..')
            sysos('python3 Ngrok.py')
        SystemClear(system=sysos)
        connect = sysos('chmod +x FreeVPNconnect.sh && bash FreeVPNconnect.sh')
        print(connect)
    mainConnect()
except KeyboardInterrupt:
    print('Good bye :)')
except ValueError:
    print(Fore.RED+'Value Error :|')