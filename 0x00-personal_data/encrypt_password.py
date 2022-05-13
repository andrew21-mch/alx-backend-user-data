#!/usr/bin/env python3
"""Encrypts and checks password validity"""

import bcrypt


def hash_password(password: str) -> bytes:
    """returns a salted, hashed password, which is a byte string."""
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Checks password validity"""
    is_valid = False
    encoded = password.encode()
    if bcrypt.checkpw(encoded, hashed_password):
        is_valid = True
    return is_valid
