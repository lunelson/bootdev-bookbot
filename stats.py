# pyright: strict
from typing import TypedDict


def get_num_words(text: str) -> int:
    return len(text.split())


def get_char_counts(text: str) -> dict[str, int]:
    char_counts: dict[str, int] = dict()
    for char in text:
        lchar = char.lower()
        if lchar not in char_counts:
            char_counts[lchar] = 0
        char_counts[lchar] += 1
    return char_counts


class CharCountDict(TypedDict):
    char: str
    num: int


def get_char_count_dicts(counts_dict: dict[str, int]) -> list[CharCountDict]:
    char_count_dicts: list[CharCountDict] = [
        {"char": char, "num": num} for char, num in counts_dict.items()
    ]
    char_count_dicts.sort(key=lambda x: x["num"], reverse=True)
    return char_count_dicts
