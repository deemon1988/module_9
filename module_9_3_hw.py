# Домашнее задание по теме "Генераторные сборки"

first = ['Strings', 'Student', 'Computers', 'vdvsdv']
second = ['Строка', 'Урбан', 'Компьютер']

min_length = min(len(first), len(second))

first_result = (len(a) - len(b) for a, b in zip(first, second) if len(a) != len(b))
second_result = (len(first[a]) == len(second[a]) for a in range(min_length))

print(list(first_result))
print(list(second_result))