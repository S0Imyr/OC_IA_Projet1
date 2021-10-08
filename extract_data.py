import csv
from random import randint


MOST_SPEAKED_LANGUAGES = ["eng", "zho", "hin", "spa", "ara", "fra"]


def extract_lines(path):
    with open(path, mode='r', encoding="utf8") as file:
        lines = file.readlines()
    return lines


def extract_labels(path):
    with open(path, mode='r', encoding="utf8") as labels_file:
        reader = csv.reader(labels_file)
        next(reader)


def filter_spoken_languages_lines(texts_path, languages_path):
    filtered_data = []
    texts_lines = extract_lines(texts_path)
    languages_lines = extract_lines(languages_path)
    if len(texts_lines) != len(languages_lines):
        print('Invalid data in entry : the two data files must have the same number of lines.')
    else:
        for line in range(len(languages_lines)):
            if languages_lines[line].strip() in MOST_SPEAKED_LANGUAGES:
                filtered_data.append([languages_lines[line].strip(), texts_lines[line]])
    return filtered_data


def choose_random_line(texts_path, languages_path):
    lines = filter_spoken_languages_lines(texts_path, languages_path)
    line = randint(0, len(lines))
    return lines[line]


if __name__ == "__main__":
    print(choose_random_line('data/x_test.txt', 'data/y_test.txt'))