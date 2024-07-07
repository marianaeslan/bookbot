def read_book(book_name):
    # open a file and read it
    with open("books/" + book_name) as f:
        return f.read()
