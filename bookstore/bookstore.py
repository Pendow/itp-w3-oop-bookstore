class Bookstore(object):
    
    def __init__(self, name):
        self.name = name
        self.books = []
        
    def get_books(self):
        return self.books

    def add_book(self,book):
        self.books.append(book)
        
    def search_books(self, title=None, author=None):
        booklist = []
        for book in self.books:
            if title and title.upper() in book.title.upper():
                booklist.append(book)
            if author and author == book.author:
                booklist.append(book)
        return booklist


class Author(object):
    
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
        self.books = []
        
    def get_books(self):
        return self.books


class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        author.books.append(self)
        
