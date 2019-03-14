import toNumericText as numt
from os import system

def runEncryption():
    system("cls")
    print("ELGAMAL CRYPTOSYSTEM ENCRYPTION: ")
    text = input("Enter the text for ElGamal Encryption: ")
    numericText = numt.textTonumeric(text)
    print(numericText)

def runDecryption():
    print("ELGAMAL CRYPTOSYSTEM DECRYPTION: ")