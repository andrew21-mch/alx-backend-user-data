#!/usr/bin/env python3
""" takes in a password string arguments and returns bytes.
    The returned bytes is a salted hash of the input password
"""
import uuid
from xml.dom import NotFoundErr
import bcrypt
from db import DB
from user import User
salt = bcrypt.gensalt()
from sqlalchemy.orm.exc import NoResultFound



def _hash_password(password: str) -> bytes:
    """Hashes a password"""
    hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers a user to the database"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            pwd = _hash_password(password)
            user = self._db.add_user(email, pwd)
            return user
        else:
            return "Error: User already exists"
    
    def valid_login(self, email: str, password: str) -> bool:
        """Checks if the password is correct"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        else:
            if bcrypt.checkpw(password.encode("utf-8"), user.hashed_password):
                return True
            else:
                return False
    
    def _generate_uuid(self) -> str:
        """Generates a uuid"""
        return str(uuid.uuid4())
    
    def create_session(self, email: str) -> str:
        """Creates a session"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        else:
            session_id = self._generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
    
    def get_user_from_session_id(self, session_id: str) -> str:
        """Returns a user based on a session id"""
        if not session_id:
            return None
        try:
            user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None
        else:
            return user
    