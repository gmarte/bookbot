def get_num_words(book_text):
    count = len(book_text.split())
    return count


def char_count(book_text):
    lower = book_text.lower()
    result = {}
    lower_set = set(lower)
    for l in lower_set:
        result[l] = lower.count(l)
    return result


