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
    # counting how many time each char appears on the book
    for char in lower_case:
        if char.isalpha():
            if char in characters:
                characters[char] +=1
            else: 
                characters[char] = 1
    return characters

def sort_dict(dictionary):
    char_list = [{'char': k, 'count': v} for k,v in dictionary.items()]
    return sorted(char_list, key=lambda x: x['count'], reverse = True)

book_name = "frankenstein.txt"
main(book_name)
print("\n")

print (f"--- Begin report of books/{book_name} ---")

total_words = count_words(book_name)
print(f"{total_words} words found in the document")
print("\n")

character_count = count_char(book_name)
sorted_characters = sort_dict(character_count)

for item in sorted_characters:
    print (f"The '{item['char']}' character was found {item['count']} times")

print("\n")
print("--- End report ---")

