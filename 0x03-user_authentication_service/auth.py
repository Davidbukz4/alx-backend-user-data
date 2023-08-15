#!/usr/bin/env python3
'''
Authentication
'''
import bcrypt


def _hash_password(password: str) -> bytes:
    ''' returns a hashed password '''
    hashed_pwd = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_pwd
