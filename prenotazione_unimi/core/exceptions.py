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


class LibraryError(Exception):
    """Raised when there's an error with the library code"""


class LibraryLoginError(LibraryError):
    """Error with the login"""


class ResourceFetchError(LibraryError):
    """Raised when timeslots can't be fetched"""


class LibraryBookingError(LibraryError):
    """Raised when there's an error with the booking"""


class SilabError(Exception):
    """Raised when there's an error with the silab code"""


class TimeslotFetchingError(SilabError):
    """Raised when the timeslots can't be fetched"""


class SilabLoginError(SilabError):
    """Raised when there's an error with the login"""


class SilabBookingError(SilabError):
    """Raised when there's an error with the booking"""
