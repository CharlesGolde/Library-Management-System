"""Main entry point for the Library Management System.

Provides an interactive CLI menu for managing the library.
"""

from library_service import LibraryService
from exceptions import (
    BookNotFoundError,
    MemberNotFoundError,
    BookUnavailableError,
    LoanNotFoundError
)


def print_menu():
    """Display the main menu options."""
    print("\n" + "="*50)
    print("     LIBRARY MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Add Book")
    print("2. Register Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. View Books")
    print("6. View Members")
    print("7. View Loans")
    print("8. Exit")
    print("="*50)


def add_book(service):
    """Feature 1: Add a new book."""
    try:
        print("\n--- Add Book ---")
        book_id = input("Enter Book ID: ").strip()
        title = input("Enter Book Title: ").strip()
        author = input("Enter Book Author: ").strip()
        
        service.add_book(book_id, title, author)
        print(f"✓ Book added: {title}")
    except ValueError as e:
        print(f"✗ Error: {e}")


def register_member(service):
    """Feature 2: Register a new member."""
    try:
        print("\n--- Register Member ---")
        member_id = input("Enter Member ID: ").strip()
        name = input("Enter Member Name: ").strip()
        email = input("Enter Member Email: ").strip()
        
        service.register_member(member_id, name, email)
        print(f"✓ Member registered: {name}")
    except ValueError as e:
        print(f"✗ Error: {e}")


def borrow_book(service):
    """Feature 3: Borrow a book."""
    try:
        print("\n--- Borrow Book ---")
        book_id = input("Enter Book ID: ").strip()
        member_id = input("Enter Member ID: ").strip()
        
        loan = service.borrow_book(book_id, member_id)
        print(f"✓ {loan.member.name} borrowed {loan.book.title}")
        print(f"  Loan ID: {loan.loan_id}")
    except (BookNotFoundError, MemberNotFoundError, BookUnavailableError) as e:
        print(f"✗ Error: {e}")


def return_book(service):
    """Feature 4: Return a borrowed book."""
    try:
        print("\n--- Return Book ---")
        loan_id = input("Enter Loan ID: ").strip()
        
        loan = service.return_book(loan_id)
        print(f"✓ {loan.member.name} returned {loan.book.title}")
        print(f"  Loan ID: {loan.loan_id}")
    except (LoanNotFoundError, ValueError) as e:
        print(f"✗ Error: {e}")


def view_books(service):
    """Feature 5: View all books."""
    print("\n--- View Books ---")
    books = service.view_books()
    
    if not books:
        print("No books found.")
        return
    
    print("\nBooks:")
    for book in books:
        print(f"  {book}")


def view_members(service):
    """Feature 6: View all members."""
    print("\n--- View Members ---")
    members = service.view_members()
    
    if not members:
        print("No members found.")
        return
    
    print("\nMembers:")
    for member in members:
        print(f"  {member}")


def view_loans(service):
    """Feature 7: View all loans."""
    print("\n--- View Loans ---")
    loans = service.view_loans()
    
    if not loans:
        print("No loans found.")
        return
    
    print("\nLoans:")
    for loan in loans:
        print(f"  {loan}")


def main():
    """Main program loop."""
    service = LibraryService()
    
    print("\n" + "="*50)
    print("Welcome to Library Management System!")
    print("="*50)
    
    while True:
        print_menu()
        choice = input("Enter your choice (1-8): ").strip()
        
        if choice == "1":
            add_book(service)
        elif choice == "2":
            register_member(service)
        elif choice == "3":
            borrow_book(service)
        elif choice == "4":
            return_book(service)
        elif choice == "5":
            view_books(service)
        elif choice == "6":
            view_members(service)
        elif choice == "7":
            view_loans(service)
        elif choice == "8":
            print("\n✓ Program closed.")
            break
        else:
            print("\n✗ Invalid choice. Please enter a number between 1-8.")


if __name__ == "__main__":
    main()
