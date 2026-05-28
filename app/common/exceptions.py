class AppException(Exception):
    def __init__(self, message: str, status_code: int = 400, errors=None):
        self.message = message
        self.status_code = status_code
        self.errors = errors


class NotFoundException(AppException):
    def __init__(self, message: str = "Resource not found", errors=None):
        super().__init__(message=message, status_code=404, errors=errors)


class UnauthorizedException(AppException):
    """
    Cuando:

    - no hay token.
    - token inválido.
    - token expirado.
    - login incorrecto.

    Ejemplo:

    - 'Invalid credentials'
    """

    def __init__(self, message: str = "Unauthorized", errors=None):
        super().__init__(message=message, status_code=404, errors=errors)


class ForbiddenException(AppException):
    """
    Cuando:

    - el usuario SÍ está autenticado.
    - pero NO tiene permisos.

    Ejemplo:

    - 'Admin permissions required'
    """

    def __init__(self, message: str = "Forbidden", errors=None):
        super().__init__(message=message, status_code=404, errors=errors)


class ConflictException(AppException):
    """
    Cuando:

    - ya existe un recurso.
    - hay conflictos de estado.

    Ejemplo:

    - Email already registered
    """

    def __init__(self, message: str = "Conflict", errors=None):
        super().__init__(message=message, status_code=404, errors=errors)
