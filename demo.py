# demo.py
from operations import *

def demo():
    print("Adding books...")
    add_book("B001", "To Kill a Mockingbird", "Harper Lee", "Penguin", "Fiction")
    add_book("B002", "The Silent Patient", "Alex Michaelides", "Orion", "Thriller")

    print("\nAdding members...")
    add_member("M001", "Kella", "Freetown")

    print("\nBorrowing book...")
    borrow_book("M001", "B001")

    print("\nReturning book...")
    return_book("M001", "B001")

    print("\n--- Final Data ---")
    print("Books:", books)
    print("Members:", members)

if __name__ == "__main__":
    demo()
