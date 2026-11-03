def get_all_dels(x: int) -> list:
    """
    Функция для поиска всех делителей числа с некоторым условием

    :param x: некоторое целое число
    :return: список целых делителей числа
    """
    d = []
    for n in range(2, int(x ** 0.5) + 1):
        if x % n == 0: # сюда НИЧЕГО дополнительно не пишем!!!
            if (n): # для дополнительных условий, вроде "только чётные делители", "только простые" и т.д.
                d.append(n)
            if (x//n):
                d.append(x // n)
    return sorted(set(d))


def isPrime(n: int) -> bool:
    """
    Функция для проверки числа n на простоту

    :param n: некоторое целое число
    :return: логический результат, простое ли число n
    """
    if n == 1: return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True



def get_all_prime_multiplier(n: int) -> list:
    """
    Получение всех простых делителей числа

    :param n: целое число
    :return: список простых делителей числа
    """
    multipliers = []
    i = 2
    num = n
    while not isPrime(num):
        if num % i == 0:
            multipliers.append(i)
            num //= i
        else:
            i += 1
    multipliers.append(num)
    return multipliers



def print_all_mask_numbers():
    """
    Код для решения задачи на поиск чисел, соответствующих определенной маске
    :return:
    """
    from fnmatch import fnmatch

    for x in range(0, 10**10, 96437):
        if fnmatch(str(x), '7?2*4??9?'):
            print(x, x//96437)