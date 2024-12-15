class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        print(f"Название книги: {self.title}\nАвтор: {self.author}\nГод издания: {self.year}")

book = Book(str(input("Введите название книги:\n")), str(input("Введите автора книги:\n")), str(input("Введите год издания:\n")))
book.get_info()