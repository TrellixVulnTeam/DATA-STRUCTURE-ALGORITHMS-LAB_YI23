from operator import attrgetter

class Book:
    def __init__(self):
        self.author = "defult text"
        self.title = "defult text"
        self.description = "defult text"
        self.availability = "defult text"

    def __repr__(self):
            return (self.title,
                                                                         self.author,
                                                                         self.description,
                                                                         self.availability)


    def set_book_info(self):
        self.title = input("Input Book Title")
        self.author = input("Input Book Author")
        self.description = input("Input Book Description")
        self.availability = input("Input Book Availability")

    def show_book_info(self):
        print("Book Informtion")
        #print(f"Title: {self.title} Author: {self.author} Description: {self.description} Availability: {self.availability}")
        print(self)

class Books:
    def __init__(self):
        self.books = list()
        self.book_titles = list()

    def add_book(self):
        book = Book()
        book.set_book_info()
        self.books.append(book)


    def add_books(self):
        number_of_books_to_be_added = int(input("How Many Books to be Inputed?"))
        for iteration in range(number_of_books_to_be_added):
            self.add_book()

    def count(self):
        print("the Total Books in the System: ",len(self.books))

        ##linear Search
    def search_available_books(self):
        available_books = list()
        for book in self.books:
            if book.availability  == "True":
                available_books.append(book)
        print(f"There are {len(available_books)} available books, the titles are displayed below")
        for book2 in available_books:
            print(book2)

    def search_books_using_title(self):
        all_books = self.books.copy()
        sorted_books = sorted(all_books, key=attrgetter("title"))
        search_key = input("Input first letter of the book you're book looking for: ")

        start = 0
        end = len(sorted_books)
        attempt = 1
        if end == 1:
            end -= 1
            self.search_title_binary(sorted_books, start, end, search_key, attempt)
        else:
            self.search_title_binary(sorted_books, start, end, search_key, attempt)

    def search_title_binary(self, sorted_books, start, end, search_key, attempt):
        if end > start:

            middle_index = (start + end - 1) // 2
            if sorted_books[middle_index].title == search_key:
                print("Attempt No. {}".format(attempt))
                print("The search was successful.")
                print("The location is on index", middle_index)
            elif sorted_books[middle_index].title > search_key:
                print("Attempt No. {}".format(attempt))
                self.search_title_binary(sorted_books, start, middle_index - 1, search_key, attempt + 1)
            elif sorted_books[middle_index].title < search_key:
                print("Attempt No. {}".format(attempt))
                self.search_title_binary(sorted_books, middle_index + 1, end, search_key, attempt + 1)
        elif end == start:
            middle_index = 0
            if sorted_books[middle_index].title == search_key:
                print("Attempt No. {}".format(attempt))
                print("The search was successful.")
                print("The location is on index", middle_index)
            else:
                print("Attempt No. {}".format(attempt))
                print("The search was unsuccessful.")


        else:
            print("Attempt No. {}".format(attempt))
            print("The search was unsuccessful.")

    def sort_books_using_author(self):
        all_books = self.books.copy()
        sorted_books = sorted(all_books, key=attrgetter("author"))
        for book in sorted_books:
            print(book)





class Menu:
    def __init__(self):
        print("Welcome to Library System")
        print("Please Select an Option.")
        print("1. Add Book")
        print("2. Count Books")
        print("3. Search All Available Books")
        print("4. Search A Book Using Book Title")
        print("5. Sort A Book Using Book Author")
# region main()
if __name__ == "__main__":
    books = Books()
    user_choice = "1"

    while user_choice == "1":
        menu = Menu()
        user_choice = input("Input Selected Option: ")
        if user_choice == "1":
            books.add_books()
        elif user_choice == "2":
            books.count()
        elif user_choice == "3":
            books.search_available_books()
        elif user_choice == "4":
            books.search_books_using_title()
        elif user_choice == "6":
            books.sort_books_using_author()

        user_choice = input("1 to Continue , 2 to Exit")
# endregion