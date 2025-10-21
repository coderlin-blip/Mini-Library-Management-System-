# Mini Library Management System
# Using lists, dictionaries, tuples, and functions

# ----------------------------
# DATA STRUCTURES
# ----------------------------

# Books: dictionary (book_id → details)
books = {}

# Members: list of dictionaries
members = []

# Genres: tuple of valid genres
genres = ("Fiction", "Non-Fiction", "Romance", "Thriller", "Mystery")


# ----------------------------
# CORE FUNCTIONS (CRUD + Borrow/Return)
# ----------------------------

def add_book(book_id, title, author, publisher, genre):
    """Add a book if ID and genre are valid."""
    if book_id in books:
        return False
    if genre not in genres:
        return False
    books[book_id] = {
        "title": title,
        "author": author,
        "publisher": publisher,
        "genre": genre,
        "available": True
    }
    return True


def add_member(member_id, name, address):
    """Add a new member if ID is unique."""
    for member in members:
        if member["member_id"] == member_id:
            return False
    members.append({
        "member_id": member_id,
        "name": name,
        "address": address,
        "borrowed_books": []
    })
    return True


def search_book(search_term):
    """Search for books by title or author."""
    results = []
    for book_id, details in books.items():
        if search_term.lower() in details["title"].lower() or search_term.lower() in details["author"].lower():
            results.append((book_id, details))
    return results


def update_book(book_id, title=None, author=None, publisher=None, genre=None):
    """Update existing book details."""
    if book_id not in books:
        return False
    if genre and genre not in genres:
        return False
    if title:
        books[book_id]["title"] = title
    if author:
        books[book_id]["author"] = author
    if publisher:
        books[book_id]["publisher"] = publisher
    if genre:
        books[book_id]["genre"] = genre
    return True


def delete_book(book_id):
    """Delete a book if it exists and is available."""
    if book_id not in books:
        return False
    if not books[book_id]["available"]:
        return False
    del books[book_id]
    return True


def borrow_book(member_id, book_id):
    """Member borrows a book (max 3)."""
    for member in members:
        if member["member_id"] == member_id:
            if len(member["borrowed_books"]) >= 3:
                return False
            if book_id in books and books[book_id]["available"]:
                books[book_id]["available"] = False
                member["borrowed_books"].append(book_id)
                return True
    return False


def return_book(member_id, book_id):
    """Return borrowed book."""
    for member in members:
        if member["member_id"] == member_id and book_id in member["borrowed_books"]:
            member["borrowed_books"].remove(book_id)
            if book_id in books:
                books[book_id]["available"] = True
            return True
    return False
