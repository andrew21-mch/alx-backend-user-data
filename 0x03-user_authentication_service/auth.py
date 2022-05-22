#!/usr/bin/env python3
""" takes in a password string arguments and returns bytes.
    The returned bytes is a salted hash of the input password
"""
import bcrypt
from db import DB
from user import User
salt = bcrypt.gensalt()


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
        """REgisters a user to the database"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            pwd = _hash_password(password)
            user = self._db.add_user(email, pwd)
            return user
        else:
            raise ValueError('User {email} already exists')
