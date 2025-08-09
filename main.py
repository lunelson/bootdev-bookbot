from stats import get_num_words, count_chars

def get_book_text(file_path):
    with open(file_path) as f:
        content = f.read()
    return content

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    num_words = get_num_words(book_text)
    print(f"{num_words} words found in the document")
    char_count = count_chars(book_text)
    print(char_count)

main()
