def main():
    book_path = "books/frankenstein.txt"
    book = get_book(book_path)
    word_count = count_of_words(book)

def get_book(path):
    with open(path) as file:
        return file.read()

def count_of_words(text):
    return len(text.split())

main()