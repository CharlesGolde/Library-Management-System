"""Custom exceptions for the Library Management System."""


class BookNotFoundError(Exception):
    """Raised when a book is not found in the library."""
    pass


class MemberNotFoundError(Exception):
    """Raised when a member is not found in the system."""
    pass


class BookUnavailableError(Exception):
    """Raised when a book is not available for borrowing."""
    pass


class LoanNotFoundError(Exception):
    """Raised when a loan record is not found."""
    pass
