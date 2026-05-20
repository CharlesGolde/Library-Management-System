"""LibraryService class for managing library operations."""

from book import Book
from member import Member
from loan import Loan
from exceptions import (
    BookNotFoundError,
    MemberNotFoundError,
    BookUnavailableError,
    LoanNotFoundError
)


class LibraryService:
    """Service class for managing library operations."""
    
    def __init__(self):
        """Initialize the library service."""
        self._books = {}  # Dictionary to store books: {book_id: Book}
        self._members = {}  # Dictionary to store members: {member_id: Member}
        self._loans = []  # List to store loans
        self._loan_counter = 0  # Counter for auto-generating loan IDs
    
    # ============= BOOK OPERATIONS =============
    
    def add_book(self, book_id, title, author):
        """Add a new book to the library.
        
        Args:
            book_id (str): Unique book identifier
            title (str): Book title
            author (str): Book author
        """
        if not book_id or not title or not author:
            raise ValueError("Book ID, title, and author cannot be empty.")
        
        if book_id in self._books:
            raise ValueError(f"Book with ID '{book_id}' already exists.")
        
        book = Book(book_id, title, author)
        self._books[book_id] = book
        return book
    
    def view_books(self):
        """Get list of all books.
        
        Returns:
            list: List of Book objects
        """
        return list(self._books.values())
    
    # ============= MEMBER OPERATIONS =============
    
    def register_member(self, member_id, name, email):
        """Register a new member to the library.
        
        Args:
            member_id (str): Unique member identifier
            name (str): Member name
            email (str): Member email
        """
        if not member_id or not name or not email:
            raise ValueError("Member ID, name, and email cannot be empty.")
        
        if member_id in self._members:
            raise ValueError(f"Member with ID '{member_id}' already exists.")
        
        member = Member(member_id, name, email)
        self._members[member_id] = member
        return member
    
    def view_members(self):
        """Get list of all members.
        
        Returns:
            list: List of Member objects
        """
        return list(self._members.values())
    
    # ============= BORROWING OPERATIONS =============
    
    def borrow_book(self, book_id, member_id):
        """Borrow a book for a member.
        
        Args:
            book_id (str): ID of book to borrow
            member_id (str): ID of member borrowing
            
        Returns:
            Loan: Created loan object
            
        Raises:
            BookNotFoundError: If book not found
            MemberNotFoundError: If member not found
            BookUnavailableError: If book already borrowed
        """
        # Lookup book
        book = self._books.get(book_id)
        if book is None:
            raise BookNotFoundError(f"Book '{book_id}' not found.")
        
        # Lookup member
        member = self._members.get(member_id)
        if member is None:
            raise MemberNotFoundError(f"Member '{member_id}' not found.")
        
        # Check availability
        if not book.available:
            raise BookUnavailableError(f"Book '{book.title}' is already borrowed.")
        
        # Borrow the book
        book.borrow()
        
        # Create loan record
        self._loan_counter += 1
        loan_id = f"L{self._loan_counter:03d}"
        loan = Loan(loan_id, book, member)
        self._loans.append(loan)
        
        return loan
    
    def return_book(self, loan_id):
        """Return a borrowed book.
        
        Args:
            loan_id (str): ID of the loan to close
            
        Returns:
            Loan: Closed loan object
            
        Raises:
            LoanNotFoundError: If loan not found
        """
        # Find the loan
        loan = None
        for l in self._loans:
            if l.loan_id == loan_id:
                loan = l
                break
        
        if loan is None:
            raise LoanNotFoundError(f"Loan '{loan_id}' not found.")
        
        if not loan.is_active:
            raise ValueError(f"Loan '{loan_id}' is already closed.")
        
        # Close the loan and mark book as available
        loan.close_loan()
        loan.book.return_book()
        
        return loan
    
    # ============= LOAN OPERATIONS =============
    
    def view_loans(self):
        """Get list of all loans.
        
        Returns:
            list: List of Loan objects
        """
        return self._loans
    
    def get_active_loans(self):
        """Get list of active (open) loans.
        
        Returns:
            list: List of active Loan objects
        """
        return [loan for loan in self._loans if loan.is_active]
    
    def get_closed_loans(self):
        """Get list of closed loans.
        
        Returns:
            list: List of closed Loan objects
        """
        return [loan for loan in self._loans if not loan.is_active]
