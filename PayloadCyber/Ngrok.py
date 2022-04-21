from os import chdir, system as sysos
from colorama import Fore
from time import sleep
from platform import uname
from IPToolz import getIP
# Cut

BannerGet = '''
  sSSSSs    sSSs  sdSS_SSSSSSbs  
 d%%%%SP   d%%SP  YSSS~S%SSSSSP  
d%S'      d%S'         S%S       
S%S       S%S          S%S       
S&S       S&S          S&S       
S&S       S&S_Ss       S&S       
S&S       S&S~SP       S&S       
S&S sSSs  S&S          S&S       
S*b `S%%  S*b          S*S       
S*S   S%  S*S.         S*S       
 SS_sSSS   SSSbs       S*S       
  Y~YSSY    YSSP       S*S       
                       SP        
                       Y         
'''
BannerGetT = '''
  sSSSSs    sSSs  sdSS_SSSSSSbs        sdSS_SSSSSSbs    sSSs   .S_sSSs    
 d%%%%SP   d%%SP  YSSS~S%SSSSSP        YSSS~S%SSSSSP   d%%SP  .SS~YS%%b   
d%S'      d%S'         S%S                  S%S       d%S'    S%S   `S%b  
S%S       S%S          S%S                  S%S       S%S     S%S    S%S  
S&S       S&S          S&S                  S&S       S&S     S%S    d*S  
S&S       S&S_Ss       S&S                  S&S       S&S     S&S   .S*S  
S&S       S&S~SP       S&S                  S&S       S&S     S&S_sdSSS   
S&S sSSs  S&S          S&S                  S&S       S&S     S&S~YSSY    
S*b `S%%  S*b          S*S                  S*S       S*b     S*S         
S*S   S%  S*S.         S*S                  S*S       S*S.    S*S         
 SS_sSSS   SSSbs       S*S                  S*S        SSSbs  S*S         
  Y~YSSY    YSSP       S*S                  S*S         YSSP  S*S         
                       SP                   SP                SP          
                       Y                    Y                 Y           
                                                                          '''

BannerGetH = '''
  sSSSSs    sSSs  sdSS_SSSSSSbs         .S    S.   sdSS_SSSSSSbs  sdSS_SSSSSSbs   .S_sSSs    
 d%%%%SP   d%%SP  YSSS~S%SSSSSP        .SS    SS.  YSSS~S%SSSSSP  YSSS~S%SSSSSP  .SS~YS%%b   
d%S'      d%S'         S%S             S%S    S%S       S%S            S%S       S%S   `S%b  
S%S       S%S          S%S             S%S    S%S       S%S            S%S       S%S    S%S  
S&S       S&S          S&S             S%S SSSS%S       S&S            S&S       S%S    d*S  
S&S       S&S_Ss       S&S             S&S  SSS&S       S&S            S&S       S&S   .S*S  
S&S       S&S~SP       S&S             S&S    S&S       S&S            S&S       S&S_sdSSS   
S&S sSSs  S&S          S&S             S&S    S&S       S&S            S&S       S&S~YSSY    
S*b `S%%  S*b          S*S             S*S    S*S       S*S            S*S       S*S         
S*S   S%  S*S.         S*S             S*S    S*S       S*S            S*S       S*S         
 SS_sSSS   SSSbs       S*S             S*S    S*S       S*S            S*S       S*S         
  Y~YSSY    YSSP       S*S             SSS    S*S       S*S            S*S       S*S         
                       SP                     SP        SP             SP        SP          
                       Y                      Y         Y              Y         Y           
                                                                                             '''
SetBox = Fore.LIGHTBLUE_EX+'''
███████╗███████╗████████╗████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗
██╔════╝██╔════╝╚══██╔══╝╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║
███████╗█████╗     ██║      ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║
╚════██║██╔══╝     ██║      ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║
███████║███████╗   ██║      ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║
╚══════╝╚══════╝   ╚═╝      ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝                                        
'''
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
    def TokenSet():
        SystemClear(system=sysos)
        def setos():
            puttoken = input(Fore.RED+'┌─['+Fore.GREEN+'Token'+Fore.YELLOW+'~'+Fore.LIGHTYELLOW_EX+'Set'+Fore.RED+Fore.RED+']'+'\n└──╼> '+Fore.WHITE)
            chdir('Ngrok')
            sysos('./ngrok authtoken '+puttoken)
            chdir('..')
            sysos('python3 Ngrok.py')
        print(SetBox)
        print(Fore.RED+'\n['+Fore.YELLOW+'1'+Fore.RED+']'+Fore.GREEN+' Set Default'+Fore.LIGHTCYAN_EX+' Token'+Fore.YELLOW+' !\n')
        print(Fore.RED+'\n['+Fore.YELLOW+'2'+Fore.RED+']'+Fore.GREEN+' Set Personal'+Fore.LIGHTCYAN_EX+' Token'+Fore.YELLOW+' !\n')
        print(Fore.RED+'\n['+Fore.YELLOW+'3'+Fore.RED+']'+Fore.GREEN+' info '+Fore.LIGHTCYAN_EX+'Set Token'+Fore.YELLOW+' ?\n\n')
        selectToken = int(input(Fore.RED+'┌─['+Fore.GREEN+'Select'+Fore.YELLOW+'~'+Fore.LIGHTYELLOW_EX+'Options'+Fore.RED+Fore.RED+']'+'\n└──╼> '+Fore.WHITE))
        if selectToken == 1:
            chdir('Ngrok')
            sysos('./ngrok authtoken 285PkcYNH2K1p2ELRNyH6mEBgib_7y7U3FSHGL8YQrR5wMbF5')
            chdir('..')
            sysos('python3 Ngrok.py')
        elif selectToken == 2:
            setos()
        elif selectToken == 3:
            chdir('Info')
            sysos('ruby infoSetToken.rb')
    # Cut
    # Cut

    def GetIp():
        SystemClear(system=sysos)
        print(Fore.RESET+BannerGet)
        def Tcp():
            SystemClear(system=sysos)
            print(Fore.CYAN+BannerGetT)
            getipT = input(Fore.RED+'┌─['+Fore.GREEN+'Tcp'+Fore.YELLOW+'~'+Fore.LIGHTYELLOW_EX+'Link'+Fore.RED+Fore.RED+']'+'\n└──╼> '+Fore.WHITE)
            Index = getipT[0:20]
            RunGetT = sysos('host '+str(Fore.RED+Index))
            sleep(2)
            sysos('python3 exploit.py')
        def Http():
            SystemClear(system=sysos)
            print(Fore.CYAN+BannerGetH)
            print(Fore.RED+'['+Fore.GREEN+'!'+Fore.RED+']'+Fore.YELLOW+' Please Do Not Include Https\n')
            getipH = input(Fore.RED+'┌─['+Fore.GREEN+'Http'+Fore.YELLOW+'~'+Fore.LIGHTYELLOW_EX+'Link'+Fore.RED+Fore.RED+']'+'\n└──╼> '+Fore.WHITE)
            showip = getIP(getipH)
            print(showip)
            sleep(2)
            sysos('python3 exploit.py')
        print(Fore.RED+'\n['+Fore.WHITE+'1'+Fore.RED+']'+Fore.LIGHTCYAN_EX+' ⟹'+Fore.WHITE+' Ngrok Tcp '+Fore.RED+'IP'+Fore.YELLOW+' !\n')
        print(Fore.RED+'\n['+Fore.WHITE+'2'+Fore.RED+']'+Fore.LIGHTCYAN_EX+' ⟹'+Fore.WHITE+' Ngrok Http '+Fore.RED+'IP'+Fore.YELLOW+' !\n')
        selects = int(input(Fore.RED+'┌─['+Fore.GREEN+'Http/Tcp'+Fore.YELLOW+'~'+Fore.LIGHTYELLOW_EX+'Link'+Fore.RED+Fore.RED+']'+'\n└──╼> '+Fore.WHITE))
        if selects == 1:
            Tcp()
        elif selects == 2:
            Http()

    print(Fore.LIGHTCYAN_EX+'''
    /$$   /$$                               /$$              /$$   /$$                       /$$    
    | $$$ | $$                              | $$             | $$  | $$                      | $$    
    | $$$$| $$  /$$$$$$   /$$$$$$   /$$$$$$ | $$   /$$       | $$  | $$  /$$$$$$   /$$$$$$$ /$$$$$$  
    | $$ $$ $$ /$$__  $$ /$$__  $$ /$$__  $$| $$  /$$//$$$$$$| $$$$$$$$ /$$__  $$ /$$_____/|_  $$_/  
    | $$  $$$$| $$  \ $$| $$  \__/| $$  \ $$| $$$$$$/|______/| $$__  $$| $$  \ $$|  $$$$$$   | $$    
    | $$\  $$$| $$  | $$| $$      | $$  | $$| $$_  $$        | $$  | $$| $$  | $$ \____  $$  | $$ /$$
    | $$ \  $$|  $$$$$$$| $$      |  $$$$$$/| $$ \  $$       | $$  | $$|  $$$$$$/ /$$$$$$$/  |  $$$$/
    |__/  \__/ \____  $$|__/       \______/ |__/  \__/       |__/  |__/ \______/ |_______/    \___/  
            /$$  \ $$                                                                             
            |  $$$$$$/                                                                             
            \______/                                                                              
    ''')
    # Cut
    def List():
        sleep(0.45)
        print(Fore.RED+'\n['+Fore.WHITE+'1'+Fore.RED+']'+Fore.LIGHTCYAN_EX+' ⟹'+Fore.WHITE+' Download '+Fore.RED+'Ngrok'+Fore.YELLOW+' !\n')
        sleep(0.25)
        print(Fore.RED+'['+Fore.WHITE+'2'+Fore.RED+']'+Fore.LIGHTCYAN_EX+' ⟹'+Fore.WHITE+' Set'+Fore.RED+' Token Ngrok'+Fore.YELLOW+' !\n')
        sleep(0.5)
        print(Fore.RED+'['+Fore.WHITE+'3'+Fore.RED+']'+Fore.LIGHTCYAN_EX+' ⟹'+Fore.WHITE+' Creator'+Fore.RED+' Ngrok'+Fore.WHITE+' Tcp'+Fore.YELLOW+' !\n')
        sleep(0.5)
        print(Fore.RED+'['+Fore.WHITE+'4'+Fore.RED+']'+Fore.LIGHTCYAN_EX+' ⟹'+Fore.WHITE+' Connect to '+Fore.RED+'Vpn'+Fore.LIGHTYELLOW_EX+' For downlaod Ngrok'+Fore.GREEN+' $\n')
        sleep(0.5)
        print(Fore.RED+'['+Fore.WHITE+'5'+Fore.RED+']'+Fore.LIGHTCYAN_EX+' ⟹'+Fore.WHITE+' Info '+Fore.RED+'Token'+Fore.LIGHTYELLOW_EX+' Ngrok'+Fore.GREEN+' ?\n')
        sleep(0.5)
        print(Fore.RED+'['+Fore.WHITE+'6'+Fore.RED+']'+Fore.LIGHTCYAN_EX+' ⟹'+Fore.YELLOW+' Get '+Fore.GREEN+'IP'+Fore.RED+' Ngrok\n\n')
        sleep(0.5)
    List()
    def Selects():
        selects = int(input(Fore.RED+'┌─['+Fore.GREEN+'Ngrok'+Fore.YELLOW+'~'+Fore.LIGHTYELLOW_EX+'HOST'+Fore.RED+Fore.RED+']'+'\n└──╼> '+Fore.WHITE))
        if selects == 1:
            sysos('python3 Ndownloads.py')
        elif selects == 2:
            TokenSet()
        elif selects == 3:
            sysos('python3 CreatorNgrok.py')
        elif selects == 4:
            chdir('Vpn')
            sysos('python3 Connect.py')
        elif selects == 5:
            chdir('Info')
            sysos('ruby infoToken.rb')
        elif selects == 6:
            GetIp()
        elif selects >= 0:
            sysos('ruby welcome.rb')
    Selects()
    # Cut
except KeyboardInterrupt:
    print('Good bye :)')
except ValueError:
    print(Fore.RED+'Value Error :|')