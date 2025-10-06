#!/usr/bin/python3

from cryptography.fernet import Fernet

def format_print(string, sep='|'):
    for char in string:
        if char == sep:
            print()
        else:
            print(char, end='')
    print()

key = input('Enter key: ')
fernet = Fernet(key)

pswd = input("Enter login information (line separator character is '|'): ")
encrypted_pswd = fernet.encrypt(bytes(pswd, 'utf-8'))
decrypted_pswd = fernet.decrypt(encrypted_pswd).decode()

assert pswd == decrypted_pswd, f'Inputted password and decrypted password do not match!\nInputted password: {pswd}\nDecrypted password: {decrypted_pswd}'

print(f'Your encrypted password is: {encrypted_pswd}')
print('This password decrypted is: ')
if ' = ' in decrypted_pswd:
    format_print(decrypted_pswd)
else:
    format_print(decrypted_pswd, sep=' ')
