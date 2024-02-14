class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def pages(self, value):
        if not isinstance(value, int):
            raise ValueError("Кол-во стр. должно быть целым.")
        if value <= 0:
            raise ValueError("Кол-во стр. должно быть положительным.")
        self._pages = value

    def __str__(self):
        return f"{super().__str__()} Кол-во страниц: {self.pages}"

    def __repr__(self):
        return f"{super().__repr__()}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def duration(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Продолжительность должна быть числом.")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительным.")
        self._duration = value

    def __str__(self):
        return f"{super().__str__()} Продолжительность: {self.duration} мин"

    def __repr__(self):
        return f"{super().__repr__()}, duration={self.duration!r})"

paper_book = PaperBook("Как закалялась сталь", "Островский", 1934)
audio_book = AudioBook("Душа Запада", "Суржиков Роман", 60.57)

print(paper_book)
print(audio_book)

