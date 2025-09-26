import sys

from stats import get_num_words

def get_book_text():
    try:
        with open(sys.argv[1]) as f: 
            file_contents = f.read()
            get_num_words()
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


def main():
    get_book_text()

main()