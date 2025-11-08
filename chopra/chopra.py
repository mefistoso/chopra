#!/usr/bin/env python3

import random
from importlib.resources import files

# Basic config options -- change as needed
SCIENTIST_FILE_PATH = "scientist.txt"
VERB_FILE_PATH = "verb.txt"
NOUN_FILE_PATH = "noun.txt"
ADJECTIVE_FILE_PATH = "adjective.txt"
SENTENCE_FILE_PATH = "sentence.txt"

def get_random_line(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    return random.choice(lines).strip()

def get_unique_lines(file, n):
    lines = set()
    while len(lines) < n:
        lines.add(get_random_line(file))
    return list(lines)

def build_quote():
    """
    Build quote/sentence by randomly sampling the globally-specified files.
    """
    with files("chopra.data_files").joinpath(SCIENTIST_FILE_PATH) as path:
        scientist = get_random_line(path)
    with files("chopra.data_files").joinpath(VERB_FILE_PATH) as path:
        verb1, verb2, verb3 = get_unique_lines(path, 3)
    with files("chopra.data_files").joinpath(NOUN_FILE_PATH) as path:
        noun1, noun2, noun3, noun4, noun5 = get_unique_lines(path, 5)
    with files("chopra.data_files").joinpath(ADJECTIVE_FILE_PATH) as path:
        adjective1, adjective2, adjective3, adjective4, adjective5 = get_unique_lines(path, 5)
    with files("chopra.data_files").joinpath(SENTENCE_FILE_PATH) as path:
        chopraline = get_random_line(path)
    chopraline = chopraline.format(
        verb1=verb1, verb2=verb2, verb3=verb3,
        noun1=noun1, noun2=noun2, noun3=noun3, noun4=noun4, noun5=noun5,
        adjective1=adjective1, adjective2=adjective2, adjective3=adjective3,
        adjective4=adjective4, adjective5=adjective5,
        scientist=scientist)

    return chopraline

if __name__ == "__main__":
    chopraline = build_quote()
    print(chopraline)

