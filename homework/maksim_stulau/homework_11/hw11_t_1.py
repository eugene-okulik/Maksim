"""Первый класс

Создайте класс book с атрибутами:

    материал страниц
    наличие текста
    название книги
    автор
    кол-во страниц
    ISBN
    флаг зарезервирована ли книга или нет (True/False).

Какие-то из атрибутов будут общими для всех книг (материал, наличие текста), какие-то индивидуальными.
Создайте несколько (штук 5) экземпляров разных книг.
После создания пометьте одну книгу как зарезервированную.
Распечатайте детали о каждой книге в таком виде:
Если книга зарезервирована:

Название: Идиот, Автор: Достоевский, страниц: 500, материал: бумага, зарезервирована

если не зарезервирована:

Название: Идиот, Автор: Достоевский, страниц: 500, материал: бумага

Второй класс

Создайте дочерний класс для первого. Это будет класс для школьных учебников. В нем будут дополнительные атрибуты:

    предмет (типа математика, история, география),
    класс (школьный класс, для которого этот учебник)(осторожно с названием переменной.
    class - зарезервированное слово),
    наличие заданий (bool)

Создайте несколько экземпляров учебников.
После создания пометьте один учебник как зарезервированный.
Распечатайте детали о каждом учебнике в таком виде: Если учебник зарезервирован:

Название: Алгебра, Автор: Иванов, страниц: 200, предмет: Математика, класс: 9, зарезервирована

если не зарезервирован:

Название: Алгебра, Автор: Иванов, страниц: 200, предмет: Математика, класс: 9"""

# from abc import abstractmethod


class Book:

    page_material = 'paper'
    presence_text = True

    def __init__(self, book_name, author, nums_page, isbn, reserved):
        self.book_name = book_name
        self.author = author
        self.nums_page = nums_page
        self.isbn = isbn
        self.reserved = reserved

    # @abstractmethod
    # def get_book(self):
    #     pass

    def get_book(self):
        if self.reserved:
            print(f"Название: {self.book_name}, Автор: {self.author}, страниц: {self.nums_page}, "
                  f"материал: {self.page_material}, зарезервирована")
        else:
            print(f"Название: {self.book_name}, Автор: {self.author}, страниц: {self.nums_page}, "
                  f"материал: {self.page_material}")


class Subjects(Book):

    subject_type = "textbooks"
    has_tasks = True

    def __init__(self, book_name, author, nums_page, isbn, subject, class_name, reserved):
        super().__init__(book_name, author, nums_page, isbn, reserved)
        self.subject = subject
        self.class_name = class_name

    def get_book(self):
        if self.reserved:
            print(f"Название: {self.book_name}, Автор: {self.author}, страниц: {self.nums_page}, "
                  f"предмет: {self.subject}, класс: {self.class_name}, зарезервирована")
        else:
            print(f"Название: {self.book_name}, Автор: {self.author}, страниц: {self.nums_page}, "
                  f"предмет: {self.subject}, класс: {self.class_name}")


book_1 = Book("Bookvar", "AB", 50, 2, False)
book_2 = Book("Second", "CD", 80, 2, False)
book_3 = Book("Green", "IF", 120, 2, False)
book_4 = Book("Sylabus", "ISTQB", 300, 2, True)
book_5 = Book("Python", "FF", 500, 2, True)

textbook_1 = Subjects("Alg", "GG", 200, 2, "Math", "7a", True)
textbook_2 = Subjects("Hist", "TT", 500, 2, "His", "8b", False)
textbook_3 = Subjects("Geo", "HF", 400, 2, "Geog", "9d", False)

book_1.get_book()
book_2.get_book()
book_3.get_book()
book_4.get_book()
book_5.get_book()

textbook_1.get_book()
textbook_2.get_book()
textbook_3.get_book()
