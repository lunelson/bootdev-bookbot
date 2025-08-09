def get_num_words(text):
    return len(text.split())


def get_char_counts(text):
    char_counts = dict()
    for char in text:
        lchar = char.lower()
        if lchar not in char_counts:
            char_counts[lchar] = 0
        char_counts[lchar] += 1
    return char_counts


def get_char_count_dicts(counts_dict):
    char_count_dicts = [{"char": char, "num": num} for char, num in counts_dict.items()]
    char_count_dicts.sort(key=lambda x: x["num"], reverse=True)
    return char_count_dicts
