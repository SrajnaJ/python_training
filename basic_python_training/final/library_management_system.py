class Book:
    def __init__(self, title, author, category):
        self.title = title
        self.author = author
        self.category = category

    def __str__(self):
        return f"Title: {self.title} is a {self.category} by {self.author}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added successfully!\n")

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"Book '{title}' removed successfully!\n")
                return
        print(f"Book '{title}' not found.\n")

    def search_book(self, keyword):
        found_books = [book for book in self.books if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower()]
        if found_books:
            print("Search Results:")
            for book in found_books:
                print(book)
        else:
            print(f"No books found for '{keyword}'.\n")

    def display_books(self):
        if self.books:
            print("Library Collection:")
            for book in self.books:
                print(book)
        else:
            print("The library has no books.\n")


def main():
    library = Library()
    
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Display Books")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            category = input("Enter book category: ")
            book = Book(title, author, category)
            library.add_book(book)
        
        elif choice == '2':
            title = input("Enter the title of the book to remove: ")
            library.remove_book(title)
        
        elif choice == '3':
            keyword = input("Enter title or author to search: ")
            library.search_book(keyword)
        
        elif choice == '4':
            library.display_books()
        
        elif choice == '5':
            print("Exiting the Library Management System. Goodbye!")
            break
        
        else:
            print("Invalid choice, please try again!\n")


if __name__ == "__main__":
    main()
