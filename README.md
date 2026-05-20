# Library Management System

A comprehensive Python-based library management system with an interactive menu-driven interface. This system allows users to manage books, members, loans, and borrowing operations.

## Features

### 1. Add Book
- Add new books to the library
- Each book has a unique ID, title, and author
- Books are marked as available by default
- **Flowchart**: `_01_add_book.svg`

### 2. Register Member
- Register library members with their information
- Each member has a unique ID, name, and email
- **Flowchart**: `_02_register_member.svg`

### 3. Borrow Book
- Members can borrow available books
- System validates book and member existence
- Checks book availability before lending
- Creates a loan record with auto-generated loan ID
- **Flowchart**: `_03_borrow_book.svg`

### 4. Return Book
- Members can return borrowed books
- Marks books as available again
- Closes the associated loan record
- **Flowchart**: `_04_return_book.svg`

### 5. View Books
- Display all books in the library
- Shows book ID, title, author, and availability status
- **Flowchart**: `_05_view_book.svg`

### 6. View Members
- Display all registered members
- Shows member ID, name, and email
- **Flowchart**: `_06_view_member.svg`

### 7. View Loans
- Display all loan records (active and closed)
- Shows loan ID, member name, book title, and loan status
- **Flowchart**: `_07_view_loan.svg`

### 8. Exit
- Gracefully close the program
- **Flowchart**: `_08_exit.svg`

## Project Structure

```
Library-Management-System/
├── main.py                 # Main entry point with menu interface
├── library_service.py      # Core library service logic
├── book.py                 # Book class definition
├── member.py               # Member class definition
├── loan.py                 # Loan class definition
├── exceptions.py           # Custom exception classes
└── README.md               # This file
```

## Classes

### Book
- `book_id`: Unique identifier
- `title`: Book title
- `author`: Book author
- `available`: Boolean (True = available, False = borrowed)
- Methods: `borrow()`, `return_book()`

### Member
- `member_id`: Unique identifier
- `name`: Member's full name
- `email`: Member's email address

### Loan
- `loan_id`: Unique identifier (auto-generated as L001, L002, etc.)
- `book`: Reference to Book object
- `member`: Reference to Member object
- `is_active`: Boolean (True = open, False = closed)
- `borrow_date`: Timestamp of borrowing
- `return_date`: Timestamp of return (None if not returned)
- Methods: `close_loan()`

### LibraryService
Core service providing:
- `add_book(book_id, title, author)`
- `view_books()`
- `register_member(member_id, name, email)`
- `view_members()`
- `borrow_book(book_id, member_id)` - Creates loan, validates inputs, handles errors
- `return_book(loan_id)` - Closes loan, marks book available
- `view_loans()`
- `get_active_loans()`
- `get_closed_loans()`

## Exception Handling

Custom exceptions for error handling:
- `BookNotFoundError`: Book doesn't exist
- `MemberNotFoundError`: Member doesn't exist
- `BookUnavailableError`: Book is already borrowed
- `LoanNotFoundError`: Loan record doesn't exist

## Usage

### Running the Program

```bash
python main.py
```

### Example Workflow

1. **Add a Book**
   ```
   Enter Book ID: B001
   Enter Book Title: Python Programming
   Enter Book Author: John Doe
   ```

2. **Register a Member**
   ```
   Enter Member ID: M001
   Enter Member Name: Jane Smith
   Enter Member Email: jane@example.com
   ```

3. **Borrow a Book**
   ```
   Enter Book ID: B001
   Enter Member ID: M001
   ```

4. **View Active Loans**
   - Display all loans showing member name, book title, and status

5. **Return a Book**
   ```
   Enter Loan ID: L001
   ```

## Error Handling

The system gracefully handles:
- Missing inputs (empty fields)
- Non-existent books or members
- Attempting to borrow unavailable books
- Attempting to return non-existent or already-closed loans

## Flowcharts

All features are documented with detailed flowcharts:
- Flowchart 1: Add Book process
- Flowchart 2: Register Member process
- Flowchart 3: Borrow Book process (with validations)
- Flowchart 4: Return Book process
- Flowchart 5: View Books process
- Flowchart 6: View Members process
- Flowchart 7: View Loans process
- Flowchart 8: Exit process

## Author

Created by: CharlesGolde

## License

This project is open source and available under the MIT License.
