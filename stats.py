def count_words(book):
    return len(book.split())

def count_ascii(book):
    book = book.lower() #capital and lowercase counted together
    char_count = {}
    for c in book:
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    return char_count

def sort_on(dict):
    return dict["num"]

def most_to_least(all_counts_dict):
    sort_list = []
    for char, count in all_counts_dict.items():
        sort_list.append({"char": char, "num": count})
    sort_list.sort(reverse=True, key=sort_on)
    return sort_list
                                     
                                     
                                     