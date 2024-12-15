# Домашнее задание по теме "Генераторы"


def all_variants(text):
    for i in range(len(text)):
        yield text[i]
    start = 0
    end = len(text) + 1
    for j in range(start + 1, end):
        if j == len(text):
            yield text
        else:
            yield text[start:j + 1]
            start += 1


text = "abc"

for i in all_variants(text):
    print(i)
