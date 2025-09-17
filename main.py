import sys


from stats import get_num_words

def get_book_text():
    with open(sys.argv) as f: 
        file_contents = f.read()
        get_num_words()


def main():
    get_book_text()

main()