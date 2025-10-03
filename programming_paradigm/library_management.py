class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
        
        
    def __repr__(self):
        return f"{self.title} by {self.author}"
        
class Library:
    def __init__(self, _books = None):
        if _books is None:
            self._books = []
        else:
            self._books = _books 
            
        
    def add_book(self, new_book):
        self._books.append(new_book)
        
        
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                self._books.remove(book)
        
    
    def return_book(self, title, author):
        if title not in self._books:
            self._books.append(title)
                
        
    
    def list_available_books(self):
        for book in self._books:
                print(book)
    

