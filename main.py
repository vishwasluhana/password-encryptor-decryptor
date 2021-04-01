import random
import re
from result import hash_data

def encryption(hash_data):
    password = list(input("Enter password: "))
    encrypted = ""
    unused_characters = list("%<}>{")
    for i in password:
        encrypted += random.choice(hash_data[i])+ random.choice(unused_characters)
    print("Encrypted password:", encrypted)

def decryption(hash_data):
    encrypted = input("Enter encrypted password: ")
    password = ""
    encrypted = re.split('[% < } > {]',encrypted)
    for i in encrypted:
        for key, value in hash_data.items():
            if i in value:
                password+= key
    print("Decrypted password:", password)

choice = int(input("1. Encrypt\n2. Decrypt\nEnter choice: "))
if choice == 1:
    encryption(hash_data)
elif choice == 2:
    decryption(hash_data)
