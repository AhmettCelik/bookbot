def main():
    book_path = "books/frankenstein.txt"
    book = get_book(book_path)

def get_book(path):
    with open(path) as file:
        return file.read()

main()