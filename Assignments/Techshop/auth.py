from exception import AuthenticationException, AuthorizationException

class AuthService:
    def authenticate_user(self, username, password):
        if username != "valid_user" or password != "valid_password":
            raise AuthenticationException("Authentication failed. Invalid credentials.")

    def authorize_user(self, user, resource):
        if user.role != "admin":
            raise AuthorizationException(f"User {user.username} is not authorized to access {resource}.")
