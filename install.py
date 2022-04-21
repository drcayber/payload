from os import system as sysos

install = '''
  8888888                   888             888 888 
    888                     888             888 888 
    888                     888             888 888 
    888   88888b.  .d8888b  888888  8888b.  888 888 
    888   888 "88b 88K      888        "88b 888 888 
    888   888  888 "Y8888b. 888    .d888888 888 888 
    888   888  888      X88 Y88b.  888  888 888 888 
  8888888 888  888  88888P'  "Y888 "Y888888 888 888 
'''

try:
    def Debian(self):
        self = sysos('sudo apt-get install python-pip')
        self = sysos('sudo apt-get install ruby')
        self = sysos('pip install colorama')
        self = sysos('pip install colorama')
        self = sysos('pip install requests')
        self = sysos('pip install IPToolz')
        self = sysos('pip install tqdm')
        self = sysos('sudo apt-get install neofetch')
        self = sysos('clear')
        self = sysos('neofetch')
        print('\n\n End Installed\n\n')

    def Arch(self):
        self = sysos('sudo pacman -S python-pip')
        self = sysos('sudo pacman -S ruby')
        self = sysos('pip install colorama')
        self = sysos('pip install requests')
        self = sysos('pip install IPToolz')
        self = sysos('pip install tqdm')
        self = sysos('sudo pacman -S neofetch')
        self = sysos('clear')
        self = sysos('neofetch')
        print('\n\n End Installed\n\n')
    def Banner(system):
        system = sysos('clear')
        print(install)
    Banner(system=sysos)

    def ListInstall():
        print('\n\n[1] Install Kali Linux\n')
        print('[2] Install Parrot OS\n')
        print('[3] Install Black Arch\n\n')
        installing = int(input('Install in : '))
        if installing == 1:
            Debian(self=sysos)
        elif installing == 2:
            Debian(self=sysos)
        elif installing == 3:
            Arch(self=sysos)
    ListInstall()
except KeyboardInterrupt:
    pass
except ValueError:
    print('\nNumber Select !')