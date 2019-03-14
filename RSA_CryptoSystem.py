import toNumericText as numt
from os import system

def runEncryption():
    system("cls")
    print("RSA CRYPTOSYSTEM ENCRYPTION: ")
    text = input("Enter the text for RSA Encryption: ")
    numericText = numt.textTonumeric(text)
    print(numericText)

def runDecryption():
    print("RSA CRYPTOSYSTEM DECRYPTION: ")