import sys
from stats import count_words, count_chars, sorted_char_count


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    contents = get_book_text(path)
    num_words = count_words(contents)
    num_chars = count_chars(contents)
    sorted_num_chars = sorted_char_count(num_chars)
    print(f"Found {num_words} total words")

    # print chars and their count
    for char_dict in sorted_num_chars:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['num']}")


main()
