from stats import get_num_words
from stats import process_file

def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    get_num_words(sys.argv[1])
    print("--------- Character Count -------")
    process_file(sys.argv[1])
    print("============= END ===============")

main()
