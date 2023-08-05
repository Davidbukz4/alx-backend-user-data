#!/usr/bin/env python3
'''
Encrypting data
'''
import bcrypt
from bcrypt import hashpw


def hash_password(password: str) -> bytes:
    ''' encrypts password and returns the password in bytes '''
    pwd = password.encode()
    hashed_pwd = hashpw(pwd, gensalt())
    return hashed_pwd
