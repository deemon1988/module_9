import itertools
from itertools import combinations

# 1
def number_piramyd(n):
    first_number = 1

    for start in range(1, n+1):
        col = start + 1
        for i in range(first_number, col):
            print(i, end=' ')
        print()


number_piramyd(5)

print()

# Чётные числа в диапазоне
def ewen(a,b):
    for i in range(a, b + 1):
        if i % 2 == 0:
            yield i

# for i in ewen(1,6):
#     print(i)

# 3. Сумма чисел, кратных 3 или 5
def summa_kratnih(n):
    numbera = []
    for i in range(1, n+1):
        if i % 3 == 0 or i % 5 == 0:
            numbera.append(i)
    yield sum(numbera)

for i in summa_kratnih(10):
    print(i)

# 4. Вывод чисел в обратном порядке
def back(n):

    for i in range(1, n + 1):
        print(n - 1)

back(10)

# 5. Таблица умножения
def multipie(n):
    for i in range (1, n + 1):
        for j in range(1, n + 1):
            print(f'{i} x {j} = {i * j}')

multipie(3)

#6 Нахождение простых чисел
def simple(n):
    for i in range(2, n+1):
        for j in range(2, n+1):
            if j > i:
                break
            else:
                if i % j == 0 and j != i:
                    break
                else:
                    if i == j:
                        print(i)
simple(15)


# 7. Индексирование строки
def index_row(text):
    for i in range(0, len(text)):
        print(f'symbol - {text[i]}, index = {i}')

index_row('python')


# 8. Генерация квадратов чисел
def square_generator(n):
    for i in range(1, n + 1):
        yield i**2

for i in square_generator(3):
    print(i, end=' ')
print()

# 9. Вывод чисел с шагом
def output_numbers_with_step(start, stop, step):
    start1 = start
    for i in range(start, stop):
        if start1 > stop:
            break
        print(start1, end=' ')
        start1 += step

output_numbers_with_step(0, 10, 3)
print()

# 10. Проверка палиндрома числа
def is_palindrom(n):
    str_n = str(n)
    str_back_n = ''
    reversed = str_n[::-1]
    print(reversed)
    for i in range(len(str_n), 0, -1):
        str_back_n += str_n[i-1]
    if str_n == str_back_n:
        return True
    else:
        return False

print(is_palindrom(121))

infinity_list_numbers = itertools.count(start=0, step=1)
print(infinity_list_numbers)
for i in infinity_list_numbers:
    print(i)
    if i == 10:
        break

# Список элементов
elements = ['a', 'b', 'c']
# Присваиваем индексы через count
for index, element in zip(itertools.count(1), elements):
    print(f"{index}: {element}")