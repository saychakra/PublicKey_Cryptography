import toNumericText as toNum
from time import sleep
from os import system
import RSA_CryptoSystem as __rsa
import ElGamal_CryptoSystem as __elg
import welcomeScreen as ws

def runRSA_cryptosystem():
    system(ws.checkPlatform())
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
    system(ws.checkPlatform())
    while(1):
        print("1. Run encryption/decryption")
        print("0. To Go Back")
        choice = int(input("Enter the choice: "))
        if choice == 1:
            __elg.main()
            while(1):
                print("\n\n1. Rerun ElGamal Encryption/Decryption")
                print("0. To Go Back")
                second_choice = int(input("Enter the choice: "))
                if second_choice == 1:
                    __elg.main()
                elif second_choice == 0:
                    return
        elif choice == 0:
            break
        else:
            print("Wrong Choice. Enter again:")
            continue