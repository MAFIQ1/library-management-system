def get_books_count(books):
    return len(books)


def add_book(books, title):
    books.append(title)
    return books


if __name__ == "__main__":
    books = ["Война и мир", "Преступление и наказание"]
    print("Количество книг:", get_books_count(books))
