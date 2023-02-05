BOOKS_DATABASE = [
    {
        "id": 1,
        "__name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "__name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id, name, pages):
        self._id = id
        self._name = name
        self._pages = pages

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def pages(self):
        return self._pages

    def __str__(self):
        return f'Книга "{self._name}"'

    def __repr__(self):
        return f'Book(id={self._id}, name={self._name!r}, pages={self._pages})'


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id=book_dict["id"], name=book_dict["__name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
