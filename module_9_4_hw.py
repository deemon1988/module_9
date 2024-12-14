# Домашнее задание по теме "Создание функций на лету"


import random

first = 'Мама мыла раму'
second = 'Рамена мало было'

result = map(lambda x, y: x == y, first, second)
print(list(result))


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding='utf-8') as file:
            list(map(lambda item: file.write(str(item) + ' '), data_set))

    return write_everything


write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])


class MysticBall():
    def __init__(self, words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)


random_words = ['А', 'это', 'уже', 'число', 5, 'в', 'списке']
by_mb = MysticBall(random_words)
print(by_mb())
