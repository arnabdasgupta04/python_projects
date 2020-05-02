import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
#import getpass

def encrypt():
    #p = getpass.getpass() 
    #message = p.encode()
    file = open('data.txt', 'rb')
    message = file.read()
    salt = b'salt_' # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
        )
    key = base64.urlsafe_b64encode(kdf.derive(message))
    file = open('key.txt', 'wb')
    file.write(key) # The key is type bytes still
    file.close()
    #print(key)
    f = Fernet(key)
    encrypted = f.encrypt(message)
    file1 = open('encrypted.txt', 'wb')
    file1.write(encrypted) # The key is type bytes still
    file1.close()
    print("Encryption done successfully !! ")
    
def decrypt():
    file = open('key.txt', 'rb')
    key  = file.read()
    f = Fernet(key)
    file = open('encrypted.txt', 'rb')
    encrypted1  = file.read() # The key will be type bytes
    file.close()
    #print(encrypted1)
    decrypted = f.decrypt(encrypted1)
    print('Your password is : '+str(decrypted.decode()))
    file1 = open('decrypted.txt', 'wb')
    file1.write(decrypted) # The key is type bytes still
    file1.close()
    
#encrypt()
decrypt()