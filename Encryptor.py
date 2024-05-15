from cryptography.fernet import Fernet
import base64
import getpass4
import os

friday = os.getcwd()
code = friday + '\\Code'

def encrypt():
    try:
        init_key = getpass4.getpass("Enter a password for encryption: ", char = '*')
        key = bytes(str(init_key*31)[:31], 'utf8')
        key = base64.urlsafe_b64encode(key)
        key = bytes(init_key[0]+str(key)[2:-2], 'utf8')
        f = Fernet(key)
    except Exception as e:
        print(e)

    list_files = []
    for (dirpath, dirnames, filenames) in os.walk(code):
        list_files += [os.path.join(dirpath, file) for file in filenames]

    for file in list_files:
        try:
            with open(file, 'rb') as original_file:
                original = original_file.read()
                encrypted = f.encrypt(original)
            with open (file, 'wb') as encrypted_file:
                encrypted_file.write(encrypted)
        except Exception as e:
            print(f"The file {file} has not been encrypted. Error:\n{e}")
            pass
            
    print("Your files have been encrypted successfully")

def decrypt():
    try:
        init_key = getpass4.getpass("Enter a password for decryption: ", char = '*')
        key = bytes(str(init_key*31)[:31], 'utf8')
        key = base64.urlsafe_b64encode(key)
        key = bytes(init_key[0]+str(key)[2:-2], 'utf8')
        f = Fernet(key)
    except Exception as e:
        print(e)

    list_files = []
    for (dirpath, dirnames, filenames) in os.walk(code):
        list_files += [os.path.join(dirpath, file) for file in filenames]
        
    for file in list_files:
        try:    
            with open(file, 'rb') as encrypted_file:
                encrypted = encrypted_file.read()
            
            decrypted = f.decrypt(encrypted)
            
            with open(file, 'wb') as decrypted_file:
                decrypted_file.write(decrypted)
            
        except Exception as e:
            print(e)
    print("Your files have been decrypted successfully")

query = input("Encrypt/Decrypt: ")
if query.lower() == "encrypt":
    encrypt()
else:
    decrypt()
