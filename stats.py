# pyright: strict
from typing import TypedDict


class CharCount(TypedDict):
    char: str
    num: int


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


def get_char_count_dicts(counts_dict: dict[str, int]) -> list[CharCount]:
    char_count_dicts: list[CharCount] = [
        {"char": char, "num": num} for char, num in counts_dict.items()
    ]
    char_count_dicts.sort(key=lambda x: x["num"], reverse=True)
    return char_count_dicts
