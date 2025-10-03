class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
        
        
    def __repr__(self):
        return f"{self.title} by {self.author}"
        
class Library:
    def __init__(self):
        self._books = []
       
        
    def add_book(self, new_book):
        self._books.append(new_book)
        
        
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                if not book._is_checked_out:
                    book._is_checked_out = True
                    return True
                return False
        return False
    
    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if book._is_checked_out:
                    book._is_checked_out = False
                    return True
                return False
        return False
        
        
    def list_available_books(self):
        for book in self._books:
                print(book)
    

