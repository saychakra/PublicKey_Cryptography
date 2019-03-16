from time import sleep
import RSA_digSig as rsa_ds
import ElGamal_digSig as el_ds
import welcomeScreen as ws
from os import system

def runRSA_digitalSignature():
    # system(ws.checkPlatform())
    while(1):
        system(ws.checkPlatform())
        print("1. Run Encryption/Decryption")
        print("0. To Go Back")
        choice = int(input("Enter the choice: "))
        if choice == 1:
            rsa_ds.main()
            while(1):
                print("\n\n1. Rerun RSA Digital Signature")
                print("0. To Go Back")
                second_choice = int(input("Enter the choice: "))
                if second_choice == 1:
                    rsa_ds.main()
                elif second_choice == 0:
                    return
        elif choice == 0:
            break
        else:
            print("Wrong Choice. Enter again:")
            continue
    

def runElGamal_digitalSignature():
    print("Running elgamal digital signature")
    sleep(2)