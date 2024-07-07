def read_book(book_name):
    # open a file and read it
    with open("books/" + book_name) as f:
        return f.read()
        
def main(book_name):
    # read book and print it
    file_contents = read_book(book_name)
    print(file_contents)

def count_words(book_name):
    # count how many words have in the book
    file_contents = read_book(book_name)
    total = 0
    for word in file_contents.split():
        total+=1
    return total

main("frankenstein.txt")

total_words = count_words("frankenstein.txt")
print(total_words)