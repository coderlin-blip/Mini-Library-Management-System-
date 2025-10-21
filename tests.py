# tests.py
from operations import *

def test_add_book():
    assert add_book("B003", "Becoming", "Michelle Obama", "Crown", "Non-Fiction") == True
    assert add_book("B003", "Becoming", "Michelle Obama", "Crown", "Non-Fiction") == False  # duplicate ID

def test_add_member():
    assert add_member("M002", "Mary James", "Bo") == True
    assert add_member("M002", "Mary James", "Bo") == False  # duplicate ID

def test_borrow_and_return():
    add_book("B004", "The Great Gatsby", "F. Scott Fitzgerald", "Scribner", "Fiction")
    add_member("M003", "David Conteh", "Makeni")
    assert borrow_book("M003", "B004") == True
    assert return_book("M003", "B004") == True

# Run tests
if __name__ == "__main__":
    test_add_book()
    test_add_member()
    test_borrow_and_return()
    print("✅ All tests passed successfully!")
