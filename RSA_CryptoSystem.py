from math import gcd
import sympy as sp # for checking if a number is prime or not

def find_e(z: int):
    e = 2
    while e < z:
        if gcd(e, z)==1:
            return e
        e += 1

def find_d(e: int, z: int):
    d = 2
    while d < z:
        if ((d*e) % z)==1:
            return d
        d += 1

def run_rsa(p: int,q: int, msg: str):
    n = p * q
    z = (p-1)*(q-1)
    e = find_e(z)
    d = find_d(e, z)

    print("Encrypting message . . .")
    # Converting plaintext to ciphertext
    cipher_text = ""
    # C = (P ^ e) % n
    for ch in msg:
        ch = ord(ch)
        cipher_text += chr((ch ** e) % n)
    print("Encrypted message: ", cipher_text)

    print("Decrypting message . . . ")
    # converting ciphertext to plaintext
    plain_text = ""
    for ch in cipher_text:
        ch = ord(ch)
        plain_text += chr((ch ** d) % n)
    print("Decrypted message: ", plain_text)

def main():
    p,q = map(int, input("Enter two coprime numbers (eg. 53 59) (separated by a space): ").split())
    print("You can enter any text, any word or a sentence.")
    msg = input("Enter the text: ")
    run_rsa(p, q, msg)

if __name__ == "__main__":
    main()