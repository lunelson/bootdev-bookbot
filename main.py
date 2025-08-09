from stats import get_num_words, get_char_counts, get_char_count_dicts


def get_book_text(file_path):
    with open(file_path) as f:
        content = f.read()
    return content


def main():
    path = "books/frankenstein.txt"
    book_text = get_book_text(path)
    num_words = get_num_words(book_text)
    char_counts = get_char_counts(book_text)
    char_count_dicts = get_char_count_dicts(char_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in char_count_dicts:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['num']}")
    print("============= END ===============")


main()
