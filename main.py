from stats import generate_report, get_char_frequency, get_num_words
from sys import argv, exit

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def main():
    if len(argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)

    filepath = argv[1]
    book_text = get_book_text(filepath)
    num_words = get_num_words(book_text)
    char_freq = get_char_frequency(book_text)
    report = generate_report(char_freq)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for charEntry in report:
        if charEntry["char"].isalpha():
            print(f"{charEntry['char']}: {charEntry['count']}")
    print("============= END ===============")

main()
