"""
Authentication utilities for JWT token management and password hashing.
"""

import os
from datetime import datetime, timedelta, timezone
from functools import wraps

import bcrypt
import jwt
from flask import jsonify, request

# JWT Configuration
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "dev-secret-key-change-in-production")
JWT_ALGORITHM = "HS256"
JWT_ACCESS_TOKEN_EXPIRE_MINUTES = 60  # 1 hour
JWT_REFRESH_TOKEN_EXPIRE_DAYS = 30  # 30 days


def hash_password(password: str) -> str:
    """Hash a password using bcrypt."""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed.decode("utf-8")


def verify_password(password: str, hashed_password: str) -> bool:
    """Verify a password against a hashed password."""
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password.encode("utf-8"))


def create_access_token(user_id: int, username: str) -> str:
    """Create a JWT access token."""
    payload = {
        "user_id": user_id,
        "username": username,
        "type": "access",
        "exp": datetime.now(timezone.utc) + timedelta(minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES),
        "iat": datetime.now(timezone.utc),
    }
    return jwt.encode(  # type: ignore[return-value]
        payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM
    )


def create_refresh_token(user_id: int, username: str) -> str:
    """Create a JWT refresh token."""
    payload = {
        "user_id": user_id,
        "username": username,
        "type": "refresh",
        "exp": datetime.now(timezone.utc) + timedelta(days=JWT_REFRESH_TOKEN_EXPIRE_DAYS),
        "iat": datetime.now(timezone.utc),
    }
    return jwt.encode(  # type: ignore[return-value]
        payload, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM
    )


def decode_token(token: str) -> dict | None:
    """Decode and verify a JWT token."""
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None


def get_token_from_header() -> str | None:
    """Extract JWT token from Authorization header."""
    auth_header = request.headers.get("Authorization")
    if not auth_header:
        return None

    try:
        scheme, token = auth_header.split()
        if scheme.lower() != "bearer":
            return None
        return token
    except ValueError:
        return None


def require_auth(f):
    """Decorator to require authentication for a route."""

    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = get_token_from_header()
        if not token:
            return jsonify({"error": "Missing authentication token"}), 401

        payload = decode_token(token)
        if not payload:
            return jsonify({"error": "Invalid or expired token"}), 401

        if payload.get("type") != "access":
            return jsonify({"error": "Invalid token type"}), 401

        # Add user info to request context
        request.user_id = payload["user_id"]  # type: ignore
        request.username = payload["username"]  # type: ignore

        return f(*args, **kwargs)

    return decorated_function


def optional_auth(f):
    """Decorator for routes that work with or without authentication."""

    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = get_token_from_header()

        if token:
            payload = decode_token(token)
            if payload and payload.get("type") == "access":
                # Add user info to request context
                request.user_id = payload["user_id"]  # type: ignore
                request.username = payload["username"]  # type: ignore
            else:
                # Invalid token, but route still works without auth
                request.user_id = None  # type: ignore
                request.username = None  # type: ignore
        else:
            # No token provided
            request.user_id = None  # type: ignore
            request.username = None  # type: ignore

        return f(*args, **kwargs)

    return decorated_function
