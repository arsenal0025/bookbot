def get_num_words(text):
    return len(text.split())

def get_num_letters(text):
    letters = {}
    for l in text.lower():
        if l in letters:
            letters[l] += 1
        else:
            letters[l] = 1
    return letters

def sort_on(dict):
    return dict["count"]

def sorted_list(char_dict):
    # Create a list of dictionaries
    chars_list = []
    for char, count in char_dict.items():
        chars_list.append({"char": char, "count": count})
    # Sort the list
    chars_list.sort(key=sort_on, reverse=True)
    return chars_list