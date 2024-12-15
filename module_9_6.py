import time


def func_generator(n):
    i = 0
    while i != n:
        yield i
        i += 1

# iter = func_generator(10)
# for i in iter:
#     print(i)

def fibonacci(n):
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result


def fibonacci_v1(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

fibo_v1 = fibonacci_v1(10)
for i in fibo_v1:
    print(i)

for i2 in fibo_v1:
    print(i2)

def fibonacci_v3():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

for value in fibonacci_v3():
    print(value)
    if value > 10 ** 6:
        break

start_time = time.time()
def read_large_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            yield line.strip()


for i in read_large_file('textfile.txt'):
    print(i)

fin_time = time.time()

print((fin_time-start_time)*1000)