# Домашнее задание по теме "Генераторы"
from itertools import combinations


def all_variants(text):
    for i in range(len(text)):
        yield text[i]
    start = 0
    for end in range(start + 1, len(text) + 1):
        if end == len(text):
            yield text
        else:
            yield text[start:end + 1]
            start += 1


text = "abc"

for i in all_variants(text):
    print(i)
