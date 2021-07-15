from flask import request
from flask_restful import wraps

from ..utils.cache import cache
from datetime import datetime

# For test endpoints
from flask_restful import Resource as Restful_Resource


def token_required(endpoint):
    """Decorator that requires the user to provide a valid token to access an endpoint"""
    @wraps(endpoint)
    def authorize(*args, **kwargs):
        # Get token_id from authorization header
        token_id = request.headers.get('Authorization')
        # No token_id in authorization header
        if not token_id:
            return "Missing token id", 401 
        token_id = token_id.removeprefix('Bearer ')
        
        # Get token from cache using token_id as key
        token = cache.get("lusciniaAuthorizationToken_" + token_id)
        if not token:
            return "Token does not exist", 401

        #Print the token data (id is not printed)
        print(token.__dict__)

        # Token is not issued for this api
        if not token.issued_for == "aristotle-api":
            return "Token not authorized for this api", 403
        
        # Current date is before the token's activation date
        if datetime.timestamp(datetime.now()) < token.timestamp:
            return "Token not active yet", 401
        
        # Token is valid, return endpoint as normal
        return endpoint(*args, **kwargs)
    return authorize


# Model token for testing
class Token:
    def __init__(self):
        self.timestamp = datetime.timestamp(datetime.now())
        self.issued_by = "aristotle" # Which service issued token (aristotle, plato, ect.)
        self.issued_to = "company_x" # 3rd party token was given to
        self.issued_for = "aristotle-api" # What service token is valid for (aristotle-api)


# Test endpoints
class TestToken(Restful_Resource):
    # Check if a token exists
    def get(self, token_id, timeout):
        token = cache.get("lusciniaAuthorizationToken_" + token_id)
        if not token:
            return "Token does not exist", 401
        return token.__dict__, 200

    # Create a token
    def post(self, token_id, timeout):
        token = Token()
        cache.set("lusciniaAuthorizationToken_" + token_id, token, timeout=timeout)
        return f"Token Created at {token.timestamp}", 201

class ProtectedRoute(Restful_Resource):
    # Token is required for all methods
    method_decorators = [token_required]

    # Token is required for certain methods
    # method_decorators = {'get': [token_required]}

    # Alternatively place above each method
    # @token_required
    def get(self):
        return "Protected get", 200

    def post(self):
        return "Protected post", 201