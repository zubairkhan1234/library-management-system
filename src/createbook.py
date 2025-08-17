class libraryModule:

    def __init__(self, allBooks):

        self.books = allBooks

    def create_book(self):

        title = input('Enter a title')
        author = input('Enter a Author name')
        number_of_copies = input('Enter a number of copies')
        available_copies = number_of_copies
        borrow_book_user = []

        self.books.append({
            'title': title,
            'author': author,
            'number_of_copies': number_of_copies,
            'available_copies': available_copies,
            'borrow_book_user': borrow_book_user
        })
    def get_all_books(self):

        return self.books

    def search_by_author(self):
        author_name = input('type author name to search books')

        for book in self.books:
            if author_name.lower() in book['author'].lower():
                print(book['author'])



    def search_by_title(self):
        author_name = input('type author name to search books')

        for book in self.books:
            if author_name.lower() in book['author'].lower():
                print(book['author'])