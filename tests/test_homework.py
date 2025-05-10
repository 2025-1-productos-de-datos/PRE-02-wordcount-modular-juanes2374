"""Autograding script for student homework."""

import os
import subprocess
def test_homework():
    """Test Word Count"""

    for path in [
        "homework/src",
        "homework/src/_internals",
        "homework/src/_internals/count_words.py",
        "homework/src/_internals/preprocess_lines.py",
        "homework/src/_internals/read_all_lines.py",
        "homework/src/_internals/split_into_words.py",
        "homework/src/_internals/write_word_counts.py",
    ]:
        if not os.path.exists(path):
            raise Exception(f"'{path}' directory does not exist")

    try:
        subprocess.run(
            ["python", "-m", "homework", "data/input", "data/output"],
            check=True,
        )
    except subprocess.CalledProcessError as e:
        raise Exception(f"Error running the homework script: {e}")

    if not os.path.exists("data/output/"):
        raise Exception("'data/output/' directory does not exist")

    results_file = "data/output/wordcount.tsv"
    if not os.path.exists(results_file):
        raise Exception(f"'{results_file}' file does not exist")

    with open(results_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        result = {}
        for line in lines:
            key, value = line.strip().split("\t")
            result[key] = int(value)

    assert result.get("analytics", 0) == 5
    assert result.get("business", 0) == 5
    assert result.get("by", 0) == 3
    assert result.get("algorithms", 0) == 0
    assert result.get("analysis", 0) == 2
