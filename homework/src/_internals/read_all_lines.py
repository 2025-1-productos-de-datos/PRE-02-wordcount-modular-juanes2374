import os

def read_all_lines(input_folder):
    all_lines = []
    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            with open(os.path.join(input_folder, filename), "r", encoding="utf-8") as f:
                all_lines.extend(f.readlines())
    return all_lines

