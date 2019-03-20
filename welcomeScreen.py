from os import system
import platform
import digitalSignature as dsig
import CryptoSys as crypt
from time import sleep

def checkPlatform():
     # detecting platform os to write the proper clear screen
    if (platform.system() == 'Windows'):
        return "cls"
    elif (platform.system() == 'Linux'):
        return "clear"

def encryptionDecryption():
    while(True):
        system(checkPlatform())
        print("Welcome to public key cryptography")
        print("1. RSA Cryptosystem")
        print("2. ElGamal Cryptosystem")
        print("0. To Go Back")
        crypt_choice = int(input("Choose your input: "))
        
        if (crypt_choice == 1):
            crypt.runRSA_cryptosystem()
            break
        elif (crypt_choice == 2):
            crypt.runElGamal_cryptosystem()
            break
        elif (crypt_choice == 0):
            break

def digitalSignature():
    while(True):
        system(checkPlatform())
        print("Welcome to public key cryptography")
        print("1. RSA Digital Signature")
        print("2. ElGamal Digital Signature")
        print("0. To Go Back")
        ds_choice = int(input("Choose your input: "))
        if (ds_choice == 1):
            dsig.runRSA_digitalSignature()
            break
        elif (ds_choice == 2):
            dsig.runElGamal_digitalSignature()
            break
        elif (ds_choice == 0):
            break

def runWelcomeScreen():
    while(True):
        system(checkPlatform())
        print("Welcome to public key cryptography")
        print("1. Encryption/Decryption")
        print("2. Digital Signature")
        print("0. To EXIT")
        inp = int(input("Choose your input: "))
        if (inp == 1):
            encryptionDecryption()
        elif (inp == 2):
            digitalSignature()
        elif (inp == 0):
            break
    exit()
