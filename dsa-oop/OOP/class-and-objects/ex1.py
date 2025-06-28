class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def get_info(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"

my_book = Book("The hobbit", "J.R.R .Tolkien", 310)
print(my_book.get_info())