import toNumericText as numt
from os import system
import math, random
from time import sleep

def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        
        x = x2- temp1 * x1
        y = d - temp1 * y1
        
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    
    if temp_phi == 1:
        return d + phi

def check_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5) + 2, 2):
        if num % n == 0:
            return False
    return True

def generate_keypair(p, q):
    errorVal = 0
    if not (check_prime(p) and check_prime(q)):
        print("Both numbers must be prime!")
        print("Enter values again...")
        sleep(2.5)
        errorVal = -1
    elif p == q:
        print("p and q cannot be equal!")
        print("Enter values again...")
        sleep(2.5)
        errorVal = -1
    n = p * q

    #Phi is the totient of n
    phi = (p-1) * (q-1)

    #Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    #Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = math.gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = math.gcd(e, phi)

    #Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)
    
    #Return public and private keypair
    #Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n), errorVal)

def encrypt(pk, plaintext):
    #Unpack the key into it's components
    key, n = pk
    plaintext = str(numt.textTonumeric(plaintext))
    #Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [(int(char) ** key) % n for char in plaintext]
    #Return the array of bytes
    return cipher

def runEncryption():
    system("cls")
    print("RSA CRYPTOSYSTEM ENCRYPTION: ")
    
    p, q = map(int, input("Enter two numbers which are co-prime (separated by space): ").strip().split())
    public, private, errorVal = generate_keypair(p, q)
    if (errorVal == -1):
        runEncryption()
    else:
        print("Generating public/private keypairs: ")
        print("Your Public Key: ", public)
        print("Your Private Key (please keep it safe for decryption): ", private)
        
        # enter the text for encryption
        text = input("Enter the text for RSA Encryption: ")
        print("Using your private key " + str(private) + " for encryption...")
        cipherText = encrypt(private, text)
        print("The message after RSA encryption: ")
        # the message is now in numeric form
        numericFinalMessage = ''.join(map(lambda x: str(x), cipherText))
        print("numerical text after encryption: ", numericFinalMessage)
        # converting the numeric message to the proper alphabatic form
        print("The final Encrypted Text:")
        print(numt.numericTotext(numericFinalMessage))
        print("\n\n")

###### Decryption ######

def decrypt(pk, ciphertext):
    #Unpack the key into its components
    key, n = pk
    #Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [str((int(char) ** key) % n) for char in ciphertext]
    #Return the array of bytes as a string
    return "".join(plain)

def runDecryption():
    print("RSA CRYPTOSYSTEM DECRYPTION: ")
    cipher = input("Enter the text for decryption: ")
    cipherVal = str(numt.textTonumeric(cipher))
    key, n = map(int, input("Enter the private key for decryption (enter k,n): ").strip().split(","))
    pk = (key, n)
    originalMsgNumeric = decrypt(pk, cipherVal)
    orignalText = numt.numericTotext(originalMsgNumeric)
    print("The original message : ", orignalText)
    