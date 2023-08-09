#!/usr/bin/env python3
'''
Basic Auth Module
'''
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    ''' Basic Auth '''
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        ''' returns the Base64 part of the Authorization header '''
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        token = authorization_header.split(' ')[-1]
        return token

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        ''' Basic - Base64 decode '''
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded_value = base64.b64decode(base64_authorization_header)
            return decoded_value.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        ''' Basic - User credentials '''
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        email, password = decoded_base64_authorization_header.split(':')
        return (email, password)
