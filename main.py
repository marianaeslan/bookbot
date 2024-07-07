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

def count_char(book_name):
    # count how many times a character appears in the string
    file_contents = read_book(book_name)
    # converting to lower case to avoid duplicates
    lower_case = file_contents.lower()
    characters = {}
    for char in lower_case:
        if char in characters:
            characters[char] +=1
        else: 
            characters[char] = 1
    return characters

main("frankenstein.txt")

total_words = count_words("frankenstein.txt")
print("Total words: ", total_words)

character_count = count_char("frankenstein.txt")
print("Character counts: ", character_count)