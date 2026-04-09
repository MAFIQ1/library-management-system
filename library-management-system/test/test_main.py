from src.main import get_books_count, add_book


def test_get_books_count():
    books = ["A", "B", "C"]
    assert get_books_count(books) == 3


def test_add_book():
    books = ["A", "B"]
    result = add_book(books, "C")
    assert len(result) == 3
    assert result[-1] == "C"