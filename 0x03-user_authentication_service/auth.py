#!/usr/bin/env python3
'''
Authentication
'''
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User


def _hash_password(password: str) -> bytes:
    ''' returns a hashed password '''
    hashed_pwd = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_pwd


class Auth:
    '''Auth class to interact with the authentication database.
    '''

    def __init__(self):
        ''' initializes Auth instance '''
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        ''' saves user to database '''
        if not email or not password:
            return None
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))
        else:
            raise ValueError('User {} already exists'.format(email))
