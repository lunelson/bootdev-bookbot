def get_num_words(text):
    return len(text.split())

def count_chars(text):
    char_dict = dict()
    for char in text:
        lchar = char.lower()
        if lchar not in char_dict:
            char_dict[lchar] = 0
        char_dict[lchar] += 1
    return char_dict
