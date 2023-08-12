#!/usr/bin/env python3
'''
Session Authentication
'''
from .auth import Auth
import uuid


class SessionAuth(Auth):
    ''' SessionAuth '''
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        ''' creates a session ID for a user_id '''
        if user_id and isinstance(user_id, str):
            self.session_id = str(uuid.uuid4())
            self.user_id_by_session_id[self.session_id] = user_id
            return self.session_id
        return None
