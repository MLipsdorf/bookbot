from stats import create_report
from stats import get_num_words
from stats import count_chars
import sys


def main():
    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    create_report(count_chars(sys.argv[1]),sys.argv[1], get_num_words(sys.argv[1]))

if __name__ == "__main__":
    main()
