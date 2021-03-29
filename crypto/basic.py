#!/usr/bin/env python3
from cryptography.fernet import Fernet

# This example uses cryptography module of python
# Generate key, encrypt and decrypt message.

key = Fernet.generate_key()
print("Key is", Fernet(key))
f = Fernet(key)
token = f.encrypt(b"Ths is test message")
print("After encrypt", token)
print("After Decrypt", f.decrypt(token))
