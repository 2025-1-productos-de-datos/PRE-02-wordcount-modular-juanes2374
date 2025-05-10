# obtain a list of files in the input directory
import os
from ._internals.write_count_words import write_count_words

def read_all_lines():
    all_lines = []
    input_file_list = os.listdir("data/input/")
    for filename in input_file_list:
        with open(f"data/input/{filename}", "r", encoding="utf-8") as f:
            lines = f.readlines()
            all_lines.extend(lines)
    return all_lines

def main():
    # Read all lines from input files
    all_lines = read_all_lines()

    # Count the frequency of each word
    counter = {}
    for line in all_lines:
        for word in line.split():
            word = word.lower().strip(".,!?")
            counter[word] = counter.get(word, 0) + 1

    # Write results to output
    write_count_words(counter)

if __name__ == "__main__":
    main()

