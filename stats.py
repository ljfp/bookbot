def count_book_words(book_as_string):
    words = book_as_string.split()
    return len(words)


def frequency_counter(book_as_string):
    characters_list = list(book_as_string)
    freq_dict = {}
    for character in characters_list:
        character = character.lower()
        if character in freq_dict:
            freq_dict[character] += 1
        else:
            freq_dict[character] = 1
    return freq_dict


def sorted_freq_counter(freq_dict):
    sorted_list = []
    for key in freq_dict:
        sorted_list.append({"char": key, "num": freq_dict[key]})
    def sort_on(freq):
        return freq["num"]
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

