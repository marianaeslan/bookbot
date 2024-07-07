def read_book(book_name):
    # open a file and read it
    with open("books/" + book_name) as f:
        return f.read()
        
def main(book_name):
    # read book and print it
    file_contents = read_book(book_name)
    print(file_contents)

