class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        if not isinstance(name, str):
            raise TypeError("Название книги должно быть строкой!")
        if not name:
            raise ValueError("Название книги не должно быть пустым!")

        if not isinstance(author, str):
            raise TypeError("Автор книги должно быть строкой!")
        if not author:
            raise ValueError("Автор книги не должно быть пустым!")

        self.__name = name
        self.__author = author

    @property
    def name(self):
        return self.__name

    @property
    def author(self):
        return self.__author

    def __str__(self):
        return f"Книга {self.__name}. Автор {self.__author}"

    def __repr__(self):
        properties = []
        for p in dir(self.__class__):
            if isinstance(getattr(self.__class__, p), property):
                properties.append(f'{p}={getattr(self, p)!r}')
        return f"{self.__class__.__name__}({', '.join(properties)})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        if not isinstance(pages, int):
            raise TypeError("Колличество страниц должно быть целым числом!")
        if pages < 0:
            raise ValueError("Колличество страниц не может быть отрицательным!")

        super().__init__(name, author)
        self.__pages = pages

    @property
    def pages(self):
        return self.__pages

    def __str__(self):
        return super().__str__() + f'. Кол-во страниц {self.__pages}'


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        if not isinstance(duration, float):
            raise TypeError("Колличество страниц должно числом с плавающей запятой!")
        if duration < 0.:
            raise ValueError("Продолжительность аудиокниги не может быть отрицательной!")

        super().__init__(name, author)
        self.__duration = duration

    @property
    def duration(self):
        return self.__duration

    def __str__(self):
        return super().__str__() + f'. Продолжительность {self.__duration}'
