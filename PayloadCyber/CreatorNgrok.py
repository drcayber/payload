from os import chdir, system as sysos
import os
from colorama import Fore
from time import sleep
from platform import uname
from RunHost import *
try:
    BannerName = Fore.RED+'''
    ,ggg, ,ggggggg,                                                
    dP""Y8,8P"""""Y8b                                     ,dPYb,    
    Yb, `8dP'     `88                                     IP'`Yb    
    `"  88'       88                                     I8  8I    
        88        88                                     I8  8bgg, 
        88        88    ,gggg,gg   ,gggggg,    ,ggggg,   I8 dP" "8 
        88        88   dP"  "Y8I   dP""""8I   dP"  "Y8gggI8d8bggP" 
        88        88  i8'    ,8I  ,8'    8I  i8'    ,8I  I8P' "Yb, 
        88        Y8,,d8,   ,d8I ,dP     Y8,,d8,   ,d8' ,d8    `Yb,
        88        `Y8P"Y8888P"8888P      `Y8P"Y8888P"   88P      Y8
                            ,d8I'                                  
                        ,dP'8I                                   
                        ,8"  8I                                   
                        I8   8I                                   
                        `8, ,8I                                   
                        `Y8P"                                    
    '''

    def SystemClear(system):
        system = uname()[0]
        if system == 'Linux':
            sysos('clear')
        else:
            sysos('cls')
            print(Fore.LIGHTRED_EX+'Script Not Run in Windows')

    def Creator():
        SystemClear(system=sysos)
        Banner = Fore.LIGHTRED_EX+'''
        8888888b.                         888b    888                          888      
        888   Y88b                        8888b   888                          888      
        888    888                        88888b  888                          888      
        888   d88P 888  888 88888b.       888Y88b 888  .d88b.  888d888 .d88b.  888  888 
        8888888P"  888  888 888 "88b      888 Y88b888 d88P"88b 888P"  d88""88b 888 .88P 
        888 T88b   888  888 888  888      888  Y88888 888  888 888    888  888 888888K  
        888  T88b  Y88b 888 888  888      888   Y8888 Y88b 888 888    Y88..88P 888 "88b 
        888   T88b  "Y88888 888  888      888    Y888  "Y88888 888     "Y88P"  888  888 
                                                        888                          
                                                    Y8b d88P                          
                                                    "Y88P"                           
        '''

        def ListNgorkRun():
            print(Banner)
            sleep(0.45)
            print(Fore.RED+'\n['+Fore.WHITE+'1'+Fore.RED+']'+Fore.LIGHTCYAN_EX+' ⟹'+Fore.WHITE+' Set Ngrok '+Fore.RED+'Tcp'+Fore.YELLOW+' !\n')
            sleep(0.25)
            print(Fore.RED+'['+Fore.WHITE+'2'+Fore.RED+']'+Fore.LIGHTCYAN_EX+' ⟹'+Fore.WHITE+' Set Ngrok '+Fore.RED+'Http / Https'+Fore.YELLOW+' !\n')
        ListNgorkRun()
        
        def Selects():
            selects = int(input(Fore.RED+'┌─['+Fore.GREEN+'Ngrok'+Fore.YELLOW+'~'+Fore.LIGHTYELLOW_EX+'Run'+Fore.RED+Fore.RED+']'+'\n└──╼> '+Fore.WHITE))
            if selects == 1:
                BotTcp()
            elif selects == 2:
                BotHttp()
        Selects()

    def List():
        SystemClear(system=sysos)
        print(BannerName)
        sleep(0.45)
        print(Fore.RED+'\n['+Fore.WHITE+'1'+Fore.RED+']'+Fore.LIGHTCYAN_EX+' ⟹'+Fore.WHITE+' Run '+Fore.RED+'Ngrok'+Fore.YELLOW+' !\n')
        sleep(0.25)
        print(Fore.RED+'['+Fore.WHITE+'2'+Fore.RED+']'+Fore.LIGHTCYAN_EX+' ⟹'+Fore.WHITE+' Warning ! '+Fore.RED+'Read the description'+Fore.RED+' !\n')
    List()
    def Selectsions():
        selections = int(input(Fore.RED+'┌─['+Fore.GREEN+'Ngrok'+Fore.YELLOW+'~'+Fore.LIGHTYELLOW_EX+'Selects'+Fore.RED+Fore.RED+']'+'\n└──╼> '+Fore.WHITE))
        if selections == 1:
            Creator()
        elif selections == 2:
            chdir('Info')
            sysos('ruby InfoTerminalRun.rb')

    Selectsions()
except KeyboardInterrupt:
    print('Good bye :)')
except ValueError:
    print(Fore.RED+'Value Error :|')