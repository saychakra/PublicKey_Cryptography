import toNumericText as toNum
from time import sleep
from os import system
import RSA_CryptoSystem as __rsa

def runRSA_cryptosystem():
    system("cls")
    while(1):
        print("1. For RSA Encryption")
        print("2. For RSA Decryption")
        print("0. To Go Back")
        enc_choice = int(input("Enter choice: "))
        if (enc_choice == 1):
            __rsa.runEncryption()
        elif (enc_choice == 2):
            __rsa.runDecryption()
        elif (enc_choice == 0):
            break
    
def runElGamal_cryptosystem():
    print("Running elgamal Cryptosystem")
    sleep(2)
