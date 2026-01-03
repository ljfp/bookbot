import sys
from stats import count_book_words, frequency_counter, sorted_freq_counter

def get_book_text(book_path):
    with open(book_path) as f:
        book_as_string = f.read()
    return book_as_string


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    frankenstein = get_book_text(book_path)
    word_count = count_book_words(frankenstein)
    character_frecuency = frequency_counter(frankenstein)
    sorted_character_frequency = sorted_freq_counter(character_frecuency )
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for letter in sorted_character_frequency:
        if not letter["char"].isalpha():
            continue
        print(f"{letter["char"]}: {letter["num"]}")
    print("============= END ===============")

main()
