from stats import get_num_words, char_count
import sys

def main():
    args = sys.argv[1:]
    arg_book = ""
    if not args:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        for a in args:
            print(a)
            arg_book = a
    counter = get_num_words(get_book_test(arg_book))
    chars = char_count(get_book_test(arg_book))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {arg_book}...")
    print("----------- Word Count ----------")    
    print(f"Found {counter} total words")
    print("--------- Character Count -------")
    for k, c in chars.items():
        print(f"{k}: {c}")

def get_book_test(path_file):
    with open(path_file) as f:
        file_contents = f.read()
    return file_contents
def count_words(book_text):
    count = len(book_text.split())
    print(f"{count} words found in the document")


if __name__ == "__main__":
    main()
