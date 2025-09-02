from src.createuser import UserModule
users = UserModule()
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

    def search_by_title(self):
        title_name = input('type author name to search books')

        for book in self.books:
            if title_name.lower() in book['title'].lower():
                print(book['title'])



    def search_by_author(self):
        author_name = input('Type author name to search books: ')
        count = 0
        search_result = []
        for book in self.books:
            if author_name.lower() in book['author'].lower():
                print(book['author'])
                search_result.append(book)
                count = count + 1
        if count > 0:
            print(f"{count} book(s) were found")
        if(count == 0 ):
            print('Data not found')
        print('=========++++++++++==============')
        print(search_result)
        
    def availabe_books(self):
        all_available_books = []
        for book in self.books:
            if (int(book["available_copies"])) > 0:
            
                all_available_books.append(book)
        if len(all_available_books) > 0:
            return all_available_books
        else:
            print('currently not available book')
    def borrow_a_book(self):
        print(users.get_users())