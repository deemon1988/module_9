def get_russian_names():
    return ['Ваня', 'Коля', 'Маша' ]

print(get_russian_names.__name__)

my_func = get_russian_names

print(my_func())
print(my_func.__name__)

def adder(args):
    res = 0
    for i in args:
        res += i
    return res

def multipie(args):
    res = 1
    for i in args:
        res *= i
    return res

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]

def high_function(numbers, func):
    print(f"Получилось: {func(numbers)}")

high_function(numbers=my_numbers, func=adder)
high_function(numbers=my_numbers, func=multipie)

def mul_by_2(x):
    return x * 2

result = map(mul_by_2, my_numbers)
print(result)
print(list(result))

def is_odd(x):
    return x % 2
# 3, 1, 4, 1, 5, 9, 2, 6
result = filter(is_odd, my_numbers)
print(result)
print(list(result))