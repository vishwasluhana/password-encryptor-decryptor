# password-encryptor-decryptor

# generator.py
It will generate random keys for all characters (upercase, lowercase, numbers, special characters). For example: 'a' = 'aw@34' something like that.

Then it will append all the generated keys into result.py file.

If result.py does not exist, it will create itself.

# check_duplicate.py
it will check if there is any duplicate key for 2 or more characters.

In such case you need to run generator.py again to generate new keys.

# main.py
It will encrypt or decrypt passwords.

# Note
Since everytime generator is generating new keys, if you have encrypted your password with old keys and generated new keys, the decryptor will not decrypt your password.

To overcome this problem, backup your result.py file for future use (to encrypt and decrypt passwords).
