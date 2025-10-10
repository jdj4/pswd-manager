#!/usr/bin/python3

from cryptography.fernet import Fernet
import json, sys, os

def format_print(string, sep='|'):
    for char in string:
        if char == sep:
            print()
        else:
            print(char, end='')
    print()

def main():
    with open('pswds.json', 'r') as fp:
        data = json.loads(fp.read())

    if len(sys.argv) > 1:
        if sys.argv[1] == '-l':
            print('Sites/Services with avaliable login information:')
            sites = sorted(data.keys())
            emails = []
            for site in sites:
                if '@' in site and '.' in site:
                    emails.append(site)
                else:
                    print(site)
            if emails != []:
                print('\nEmail addresses with available passwords:')
                for email in emails:
                    print(email)
        else:
            print('Usage: -l to show available sites with login info, enter no argument to get login info.')
    else:
        key = input('Enter key: ')
        fernet = Fernet(key)
        site = input('Enter site/service to get login info: ').lower()
        try:
            encrypted_pswd = bytes(data[site], 'utf-8')
            decrypted_pswd = fernet.decrypt(encrypted_pswd).decode()
            if ' = ' in decrypted_pswd:
                format_print(decrypted_pswd)
            else:
                format_print(decrypted_pswd, sep=' ')
        except KeyError:
            print(f"Error: site/service '{site}' does not exist in the data.", file=sys.stderr)
            sys.exit(1)

if __name__ == '__main__':
    main()
