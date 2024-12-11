# Домашнее задание по теме "Списковые, словарные сборки"

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

list1 = [len(x) for x in first_strings if len(x) > 4]
print(list1)

list2 = [(x, y) for x in first_strings for y in second_strings if len(x) == len(y)]
print(list2)

list3 = {i: len(i) for i in first_strings + second_strings if len(i) % 2 == 0}
print(list3)
