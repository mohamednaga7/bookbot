from stats import num_of_words, get_book_text, get_sorted_characters, num_of_characters
from report import print_report
import sys

def main():
    print(sys.argv)

    if len(sys.argv) < 2:
        print("Please provide the path to the book file as a command-line argument.")
        print('Usage: python3 main.py <path_to_book>')
        return sys.exit(1)
    
    book_path = sys.argv[1]
    # book_path = 'books/frankenstein.txt'
    book_text = get_book_text(book_path)
    word_count = num_of_words(book_text)
    chars_dict = num_of_characters(book_text)
    character_counts = get_sorted_characters(chars_dict)
    print_report(book_path, word_count, character_counts)

if __name__ == '__main__':
    main()