class EasystaffError(Exception):
    """Raised when it's not this script's fault but the server's"""


class TokenRetrivalError(EasystaffError):
    """Raised when the token for authentication couldn't be fetched"""


class LoginError(EasystaffError):
    """Login credentials were incorrect or any kind of error during login"""


class LessonsFetchingError(EasystaffError):
    """Raised when the page with the lessons can't be fetched"""


class BookingError(EasystaffError):
    """Raised when there's an error during the booking"""
