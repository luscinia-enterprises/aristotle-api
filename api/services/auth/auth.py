from flask import request
from flask_restful import wraps

from ..utils.cache import cache

# FOR TESTING
from flask_restful import Resource as Restful_Resource
from datetime import datetime


def token_required(func):
    @wraps(func)
    def authorize(*args, **kwargs):
        token_id = request.headers.get('Authorization')
        token_id = token_id.removeprefix('Bearer ')
        if not token_id:
            return "Missing token id", 400 
        
        token = cache.get(token_id)
        if not token:
            return "Token does not exist", 400

        if not token.issued_for == "aristotle-api":
            return "Token not authorized for this api", 401
        
        if datetime.timestamp(datetime.now()) < token.timestamp:
            return "Token not active yet"

        return func(*args, **kwargs)
    return authorize


# Model token for testing
class Token:
    def __init__(self):
        self.timestamp = datetime.timestamp(datetime.now())
        self.issued_by = "Aristotle" # Which service issued token (Aristotle, Plato, ect.)
        self.issued_to = "Company" # 3rd party token was given to
        self.issued_for = "aristotle-api" # What service token is valid for (aristotle-api)


# Test endpoints
class TestToken(Restful_Resource):
    # Check if a token exists
    def get(self, key, timeout):
        token = cache.get(key)
        if not token:
            return "Token does not exist", 400
        return token.__dict__, 200

    # Create a token
    def post(self, key, timeout):
        token = Token()
        cache.set(key, token, timeout=timeout)
        return f"Token Created at {token.timestamp}", 201

class ProtectedRoute(Restful_Resource):
    method_decorators = {'get': [token_required]}

    def get(self):
        return "Protected get", 200

    def post(self):
        return "Protected post", 201



