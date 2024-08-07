def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(chars_dict_to_sorted_list(number_of_times(file_contents)))

def count_of_words(str):
    return len(str.split())

def number_of_times(str):
    lowed_str = str.lower()
    chars_and_counts = {}
    for char in lowed_str:
        if char in chars_and_counts:
            chars_and_counts[char] += 1
        else:
            chars_and_counts[char] = 1
    return chars_and_counts

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()