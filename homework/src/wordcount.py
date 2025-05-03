#obtain a list of files in the input directory
import os


def read_all_lines():
    all_lines = []
    input_file_list = os.listdir("data/input/")
    for filename in input_file_list:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
            all_lines.extend(lines)
    return all_lines


def main():

    ##
    input_file_list = os.listdir("data/input/")
    # all_lines = read_all_lines()

    ## read all lines
    ## preprocess lines
    ## split in words
    ## count words
    ## write count words

    # count the frequency of the words in the files in the input directory
    counter = {}
    for filename in input_file_list:
        with open("data/input/" + filename) as f:
            for l in f:
                for w in l.split():
                    w = w.lower().strip(",.!?")
                    counter[w] = counter.get(w, 0) + 1

    ##
    # create the directory output/ if it doesn't exist
    write_count_words(counter)


def write_count_words(counter):
    if not os.path.exists("data/output"):
        os.makedirs("data/output")

    ##
    # save the results using tsv format
    with open("data/output/results.tsv", "w", encoding="utf-8") as f:
        for key, value in counter.items():
            # write the key and vlue to tahe file
            f.write(f"{key}\t{value}\n")


if __name__ == "__main__":
    main()

    
    
    