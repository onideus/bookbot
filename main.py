from stats import get_num_words, get_num_characters, get_sorted_counts
import sys


def get_book_text(book_location) -> str:
    with open(book_location) as f:
        book_text = f.read()
        return book_text


def main():
    print("============ BOOKBOT ============")

    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_location = sys.argv[1]

    book_text = get_book_text(book_location)
    num_words = get_num_words(book_text)
    num_characters = get_num_characters(book_text)
    sorted_char_counts = get_sorted_counts(num_characters)

    print(f"Analyzing book found at {book_location}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_char_counts:
        if str(item["char"]).isalpha():
            print(f"{item['char']}: {item['count']}")


main()
