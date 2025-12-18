def count_words(string):
    return len(string.split())


def count_chars(string):
    char_dict = {}
    for char in string.lower():
        if not char_dict.get(char):
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict


def sorted_char_count(char_dict):
    count_dict = [{"char": key, "num": char_dict[key]} for key in char_dict]
    count_dict.sort(reverse=True, key=lambda nums: nums["num"])
    return count_dict
