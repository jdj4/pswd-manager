# Password Manager
A simple command-line password manager for local storage. Encrypted password login information can be stored in `pswds.json` with the site/service name as the key and the encrypted login information as the value.

### Usage
* `generate_key.py`: Can create an encryption key that can be used to encrypt/decrypt data. Keep the key you use safe and private.
* `pswd_encr.py`: Can be used to encrypt the login information using the key. Enter information, using '|' as an optional line break character.
* `pswds.py`: Will decrypt information from `pswds.json`. The `-l` flag will list the current sites/services in the data. Otherwise enter the site/service name and retrieve the decrypted information.
* An example has been provided in the included `pswds.json` file using the encryption key `YEw-uozAjA2tlfnTvGZicPPFNim2gFoq29GAFPr2wOw=`.

These files can be added to the PATH for ease of use.
