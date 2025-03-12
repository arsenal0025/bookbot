from stats import get_num_words

def main():
    book_text = get_book_text()
    word_count = get_num_words(book_text)
    print(f"{word_count} words found in the document")

def get_book_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents


main()