class Book:
    def __init__(self, title: str, author: str, pages: int, price: float) -> None:
        self._title = title
        self._author = author
        self._pages = pages
        self.price = price

    # representation of our object when
    # we print it out in a string.
    def __str__(self) -> str:
        return f"{self._title} by {self._author}"

    # two books are considered equal if their titles match
    def __eq__(self, other: "Book") -> bool:
        return self._title == other._title

    # one book is "greater than" another if it costs more
    def __gt__(self, other: "Book") -> bool:
        return self.price > other.price

    # one book is "less than" another if it costs less
    def __lt__(self, other: "Book") -> bool:
        return self.price < other.price
