def split_into_words(all_lines):
    words = []
    for line in all_lines:
        words.extend(line.split())
    return words
