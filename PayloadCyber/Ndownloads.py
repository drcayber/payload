from os import chdir, system as sysos
from colorama import Fore
from time import sleep
from platform import uname
from Getdata import *
from tqdm import tqdm
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

    print(Fore.LIGHTCYAN_EX+'''
    ****     **   ********  *******     *******   **   **
    /**/**   /**  **//////**/**////**   **/////** /**  ** 
    /**//**  /** **      // /**   /**  **     //**/** **  
    /** //** /**/**         /*******  /**      /**/****   
    /**  //**/**/**    *****/**///**  /**      /**/**/**  
    /**   //****//**  ////**/**  //** //**     ** /**//** 
    /**    //*** //******** /**   //** //*******  /** //**
    //      ///   ////////  //     //   ///////   //   // 
    ''')

    def List():
        sleep(0.45)
        print(Fore.RED+'\n['+Fore.WHITE+'1'+Fore.RED+']'+Fore.LIGHTCYAN_EX+' ⟹'+Fore.WHITE+' Download'+Fore.RED+' Ngrok'+Fore.WHITE+' Debian'+Fore.GREEN+' 64'+Fore.YELLOW+' ⇣\n')
        sleep(0.45)
        print(Fore.RED+'['+Fore.WHITE+'2'+Fore.RED+']'+Fore.LIGHTCYAN_EX+' ⟹'+Fore.WHITE+' Download'+Fore.RED+' Ngrok'+Fore.WHITE+' Debian'+Fore.GREEN+' 32'+Fore.YELLOW+' ⇣\n')
        sleep(0.45)
        print(Fore.RED+'['+Fore.WHITE+'3'+Fore.RED+']'+Fore.LIGHTCYAN_EX+' ⟹'+Fore.WHITE+' Download'+Fore.RED+' Ngrok'+Fore.WHITE+' Arm'+Fore.GREEN+' 64'+Fore.YELLOW+' ⇣\n')
        sleep(0.45)
        print(Fore.RED+'['+Fore.WHITE+'4'+Fore.RED+']'+Fore.LIGHTCYAN_EX+' ⟹'+Fore.WHITE+' Download'+Fore.RED+' Ngrok'+Fore.WHITE+' Arm'+Fore.GREEN+' 32'+Fore.YELLOW+' ⇣\n')
    List()

    def Selects():
        selects = int(input(Fore.RED+'┌─['+Fore.GREEN+'Ngrok'+Fore.YELLOW+'~'+Fore.LIGHTYELLOW_EX+'Downloads'+Fore.RED+Fore.RED+']'+'\n└──╼> '+Fore.WHITE))
        if selects == 1:
            print('\n')
            for i in tqdm(range(3)):
                sleep(0.10)
            print(Fore.RED+'\n['+Fore.GREEN+'Please Wait'+Fore.RED+']\n')
            Linux64()
        elif selects == 2:
            print('\n')
            for i in tqdm(range(3)):
                sleep(0.10)
            print(Fore.RED+'\n['+Fore.GREEN+'Please Wait'+Fore.RED+']\n')        
            Linux32()
        elif selects == 3:
            print('\n')
            for i in tqdm(range(3)):
                sleep(0.10)
            print(Fore.RED+'\n['+Fore.GREEN+'Please Wait'+Fore.RED+']\n')        
            Arm64()
        elif selects == 4:
            print('\n')
            for i in tqdm(range(3)):
                sleep(0.10)
            print(Fore.RED+'\n['+Fore.GREEN+'Please Wait'+Fore.RED+']\n')
            Arm32()
        elif selects >= 0:
            sysos('python3 payloads.py')
    Selects()
    # Cut
    SystemClear(system=sysos)
    # Cur
    print(Fore.LIGHTGREEN_EX+'''
    8888888888               888        888b    888                          888      
    888                      888        8888b   888                          888      
    888                      888        88888b  888                          888      
    8888888    88888b.   .d88888        888Y88b 888  .d88b.  888d888 .d88b.  888  888 
    888        888 "88b d88" 888        888 Y88b888 d88P"88b 888P"  d88""88b 888 .88P 
    888        888  888 888  888 888888 888  Y88888 888  888 888    888  888 888888K  
    888        888  888 Y88b 888        888   Y8888 Y88b 888 888    Y88..88P 888 "88b 
    8888888888 888  888  "Y88888        888    Y888  "Y88888 888     "Y88P"  888  888 
                                                        888                          
                                                    Y8b d88P                          
                                                    "Y88P"                           
    ''')
    def Creator():
        sleep(2)
        chdir('..')
        sysos('python3 Ngrok.py')
    Creator()
except KeyboardInterrupt:
    print('Good bye :)')
except ValueError:
    print(Fore.RED+'Value Error :|')