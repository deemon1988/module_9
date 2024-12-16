#  Домашнее задание по теме "Декораторы"

def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        for i in range(2, result + 1):
            if result % i == 0 and i == result:
                return 'Простое'
            else:
                if result % i == 0:
                    return 'Составное'
                continue

    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)

result = sum_three(1, 4, 6)
print(result)
