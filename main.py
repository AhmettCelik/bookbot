def main():
    book_path = "books/frankenstein.txt"
    book = get_book(book_path)
    word_count = count_of_words(book)
    chars_dict = get_chars_count(book)
    sorted_chars = sorted_dict(chars_dict)
    print(sorted_chars)

def get_book(path):
    with open(path) as file:
        return file.read()

def count_of_words(text):
    return len(text.split())

def get_chars_count(text):
    lowered_str = text.lower()
    chars_and_counts = {}
    for char in lowered_str:
        if char in chars_and_counts:
            chars_and_counts[char] += 1
        else:
            chars_and_counts[char] = 1
    return chars_and_counts

def sort_on(dict):
    return dict["number"]

def sorted_dict(chars_dict):
    sorted_list = []
    for char in chars_dict:
        sorted_list.append({"char": char, "number": chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()