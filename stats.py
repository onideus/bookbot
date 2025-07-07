def get_num_words(book_text: str) -> int:
    return len(book_text.split())


def get_num_characters(book_text: str) -> dict:
    char_counts = {}
    for word in book_text.lower().split():
        for char in word:
            if char not in char_counts:
                char_counts[char] = 0
            char_counts[char] += 1

    return char_counts


def sort_on(items) -> list[dict]:
    return items["count"]


def get_sorted_counts(char_counts: dict) -> list[dict]:
    sorted_char_counts = []

    for char in char_counts:
        sorted_char_counts.append({"char": char, "count": char_counts[char]})

    sorted_char_counts.sort(key=sort_on, reverse=True)

    return sorted_char_counts
