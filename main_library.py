class LibraryManagementSystem:
    def __init__(self):
        self.books = []
        self.users = []
        self.authors = []
        self.genres = []

    def display_main_menu(self):
        print("Welcome to the Library Management System!")
        print("Main Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Genre Operations")
        print("5. Quit")

    def display_book_operations_menu(self):
        print("\nBook Operations:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book")
        print("5. Display all books")

    def display_user_operations_menu(self):
        print("\nUser Operations:")
        print("1. Add a new user")
        print("2. View user details")
        print("3. Display all users")

    def display_author_operations_menu(self):
        print("\nAuthor Operations:")
        print("1. Add a new author")
        print("2. View author details")
        print("3. Display all authors")

    def display_genre_operations_menu(self):
        print("\nGenre Operations:")
        print("1. Add a new genre")
        print("2. View genre details")
        print("3. Display all genres")

    def run(self):
        while True:
            self.display_main_menu()
            choice = input("Enter your choice: ")
            if choice == '1':
                self.display_book_operations_menu()
            elif choice == '2':
                self.display_user_operations_menu()
            elif choice == '3':
                self.display_author_operations_menu()
            elif choice == '4':
                self.display_genre_operations_menu()
            elif choice == '5':
                print("Exiting the Library Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    lms = LibraryManagementSystem()
    lms.run()
