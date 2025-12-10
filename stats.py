def get_book_text(book_path):
    with open(book_path, 'r', encoding='utf-8') as file:
        return file.read()


def num_of_words(text):
    words = text.split()
    return len(words)


def num_of_characters(text):
    characters = {}
    for char in text:
        char = char.lower()
        if char is not ' ' and char is not '\n':
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
    return characters


def _create_list_of_dictionaries(letters_dict):
    list_of_dicts = []
    for letter, count in letters_dict.items():
        list_of_dicts.append({'char': letter, 'num': count})
    return list_of_dicts


def get_sorted_characters(letters_dict):
    list_of_dicts = _create_list_of_dictionaries(letters_dict)
    sorted_list = sorted(list_of_dicts, key=lambda x: x['num'], reverse=True)
    return sorted_list