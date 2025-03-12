from stats import get_num_words
from stats import get_num_letters
from stats import sorted_list
import sys

def main():

    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    book_text = get_book_text(path)
    word_count = get_num_words(book_text)
    Letter_count = get_num_letters(book_text)
    sorterd_list_dict = sorted_list(Letter_count)
   
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorterd_list_dict:
        char = item["char"]
        count = item["count"]
        if char.isalpha():
            print(f":{char}: {count}")

    print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents




main()