



my_func = lambda x,y:x==y
print(my_func(2,2))
print(my_func.__name__)

my_numbers = [3, 1, 4, 1, 5, 9, 2, 6]
my_numbers_2 = [3, 1, 4, 1, 5, 9, 2, 6]
res1 = map(lambda x,y: x*y , my_numbers,my_numbers_2)
print(list(res1))

class multipier_exception(Exception):
    def __init__(self, message):
        self.message = message

def multiplier_v1(n):
    if n == 2:
        def multiplier(x):
            return x * 2
    elif n == 3:
        def multiplier(x):
            return x * 3
    else:
        raise multipier_exception ("I can call only twice functions")
    return multiplier

by_2 = multiplier_v1(2)
print(by_2.__name__)
result = map(by_2, my_numbers)
print(list(result))
by_3 = multiplier_v1(3)
result = map(by_3, my_numbers)
print(list(result))

try:
    print(multiplier_v1(26))
except multipier_exception as exc:
        print(exc.message)

def get_multiplier_v2(n):
    def multiplier(x):
        return x * n
    return multiplier

by_5 = get_multiplier_v2(5)
result = map(by_5, my_numbers)
print(list(result))