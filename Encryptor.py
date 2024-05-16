from cryptography.fernet import Fernet
import base64
import getpass4
import os

friday = os.getcwd()
code = friday + '\\Code'
print("""
This program shall be used to encrypt or decrypt the contents inside the primary 'Code' folder.
The important source code files, DLL's and other required modules and dependencies of F.R.I.D.A.Y.
lives inside the 'Code' folder. Therefore, it is essential to remember the passcode used while
encrypting the folder.
      
Proceed with utmost caution. The encrypted files cannot be recovered without the passcode used when encrypting.

""")

def checkfile():
    file = code + "/Experimental.py"
    with open (file, 'r') as text:
        state = text.readline().strip('\n')
        if state == "import webbrowser":
            print("The contents inside the 'Code' folder are currently not encrypted.")
            response = input("Do you wish to encrypt the contents for increased security.  Y[es]/N[o]: ").lower()
            if response == 'y':
                encrypt()
            elif response == 'n':
                exit()
            else:
                print('You have entered the incorrect input. Restart the program.')
                os.system('pause')
        
        else:
            print("The contents of the folder are currently encrypted.")
            response = input("Do you wish to decrypt the folder to access the source code.  Y[es]/N[o]: ").lower()
            if response == 'y':
                decrypt()
            elif response == 'n':
                exit()
            else:
                print('You have entered the incorrect input. Restart the program.')
                os.system('pause')

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
            
    print("Your files have been encrypted successfully.")
    os.system("pause")

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
    print("Your files have been decrypted successfully.")
    os.system("pause")

if __name__ == '__main__':
    checkfile()