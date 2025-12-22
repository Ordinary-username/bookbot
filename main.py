import sys
from stats import (
    count_words, 
    count_ascii, 
    most_to_least,
)

def main():
    
    if len(sys.argv)<2:
        print("No book file path detected. Usage: python3 main.py <path_to_book>. Closing")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    char_count = count_ascii(book_text)
    char_count = most_to_least(char_count)
    print_report(book_path, char_count, num_words)
    sys.exit(0)
    

def print_report(book_path, char_count, num_words):    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in char_count:
        if not dict['char'].isalpha():
            continue
        print(f"{dict['char']}: {dict['num']}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()