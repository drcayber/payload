import requests
import os
# Cut
def Linux64():
    os.chdir('Ngrok')
    url = 'https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.zip'
    downlod = requests.get(url, allow_redirects=True)
    open('ngrok-v3-stable-linux-amd64.zip', 'wb').write(downlod.content)
    os.system('unzip ngrok-v3-stable-linux-amd64.zip')
    os.remove('ngrok-v3-stable-linux-amd64.zip')
# Cut
def Linux32():
    os.chdir('Ngrok')
    url = 'https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-386.zip'
    downlod = requests.get(url, allow_redirects=True)
    open('ngrok-v3-stable-linux-386.zip', 'wb').write(downlod.content)
    os.system('unzip ngrok-v3-stable-linux-386.zip')
    os.remove('ngrok-v3-stable-linux-386.zip')
# Cut
def Arm64():
    os.chdir('Ngrok')
    url = 'https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-arm.zip'
    downlod = requests.get(url, allow_redirects=True)
    open('ngrok-v3-stable-linux-arm.zip', 'wb').write(downlod.content)
    os.system('unzip ngrok-v3-stable-linux-arm.zip')
    os.remove('ngrok-v3-stable-linux-arm.zip')
# Cut
def Arm32():
    os.chdir('Ngrok')
    url = 'https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-arm64.zip'
    downlod = requests.get(url, allow_redirects=True)
    open('ngrok-v3-stable-linux-arm64.zip', 'wb').write(downlod.content)
    os.system('unzip ngrok-v3-stable-linux-arm64.zip')
    os.remove('ngrok-v3-stable-linux-arm64.zip')