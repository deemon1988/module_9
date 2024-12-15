import time


# start_time = time.time()

def fibonacci(n):
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result


# for value in fibonacci(n=10000):
#     print(value)
#
# fin_time = time.time()
# print((fin_time-start_time)*1000)

class Fibonacci:
    def __init__(self, n):
        self.i, self.a, self.b, self.n = 0, 0, 1, n

    def __iter__(self):
        self.i, self.a, self.b = 0, 0, 1
        return self

    def __next__(self):
        self.i += 1
        if self.i > 1:
            if self.i > self.n:
                raise StopIteration()
            self.a, self.b = self.b, self.a + self.b
        return self.a

start_time = time.time()

fib_iter = Fibonacci(10000)
for value in fib_iter:
    print(value)

fin_time = time.time()

print((fin_time-start_time)*1000)