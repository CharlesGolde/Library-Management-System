"""Loan class for the Library Management System."""

from datetime import datetime


class Loan:
    """Represents a loan record for a borrowed book."""
    
    def __init__(self, loan_id, book, member):
        """Initialize a loan.
        
        Args:
            loan_id (str): Unique identifier for the loan
            book (Book): Book object being borrowed
            member (Member): Member borrowing the book
        """
        self.loan_id = loan_id
        self.book = book
        self.member = member
        self.is_active = True
        self.borrow_date = datetime.now()
        self.return_date = None
    
    def close_loan(self):
        """Close the loan (book returned)."""
        self.is_active = False
        self.return_date = datetime.now()
    
    def __str__(self):
        """String representation of the loan."""
        status = "Active" if self.is_active else "Closed"
        return f"{self.loan_id} - {self.member.name} borrowed {self.book.title} [{status}]"
