from os import system
import platform
from time import sleep
import loadingScreen as lScreen
import welcomeScreen as ws

print("############ Operating System used and preferred: Windows 10 (64 bit) ###############")
print("\nChecking your Operating System . . .")
os_ver = platform.system()
if os_ver == 'Windows':
    print("\nOS: Windows")
    sleep(1)
    system("cls")
elif os_ver == 'Linux':
    print("OS: Linux")
    raise("exe files not supported on Linux")
print("##################### Python version used: Python 3.7.2 #########################")
print("Checking your python version... ")
sleep(1)
cmd_out = system("python3 --version")
if (cmd_out == 0):
    print("\nYou are are good to go!")
    sleep(1)
    system("cls")
    print("Preparing the program . . . Please wait . . .")
    sleep(2)
    system("cls")
else:
    print("Please install python 3 and then continue or check if python3 is installed by any other name")
    exit()

print("Installing packages required for project")
print("\nInstalling sympy for checking prime verification")
cmd_out2 = system("python3 -m pip install sympy")
if cmd_out2 == 0:
    print("\nAll modules installed!")
    print("\nPlease wait . . . DO NOT EXIT . . .")
    sleep(2)
    system("cls")
    lScreen.loadScreen()
    ws.runWelcomeScreen()
else:
    print("\nModules could not be installed")
    print("Please try a manual installation and try again")
    print("Exiting program")
    sleep(4)
    exit()