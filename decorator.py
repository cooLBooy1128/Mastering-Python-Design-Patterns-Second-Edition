import functools
from timeit import Timer


def memorize(fn):
    cache = {}

    @functools.wraps(fn)
    def memorizer(*args):
        """缓存装饰器"""
        if args not in cache:
            cache[args] = fn(*args)
            # print(cache)
        return cache[args]

    return memorizer


def number_sum(n):
    """返回前n个数字的和"""
    assert n >= 0, 'n must be >= 0'
    if n == 0:
        return 0
    return n + number_sum(n - 1)


def fibonacci(n):
    """返回斐波那契数列的第n个数"""
    assert n >= 0, 'n must be >= 0'
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@memorize
def number_sum_memo(n):
    """返回前n个数字的和（使用缓存）"""
    assert n >= 0, 'n must be >= 0'
    if n == 0:
        return 0
    return n + number_sum_memo(n - 1)


@memorize
def fibonacci_memo(n):
    """返回斐波那契数列的第n个数（使用缓存）"""
    assert n >= 0, 'n must be >= 0'
    if n in (0, 1):
        return n
    return fibonacci_memo(n - 1) + fibonacci_memo(n - 2)


def main():
    to_execute = [(number_sum, Timer('number_sum(30)', 'from __main__ import number_sum')),
                  (fibonacci, Timer('fibonacci(10)', 'from __main__ import fibonacci')),
                  (number_sum_memo, Timer('number_sum_memo(30)', 'from __main__ import number_sum_memo')),
                  (fibonacci_memo, Timer('fibonacci_memo(10)', 'from __main__ import fibonacci_memo'))]
    for fn, t in to_execute:
        print(f'Function "{fn.__name__}": {fn.__doc__}')
        print(f'Time: {t.timeit()}s')


if __name__ == '__main__':
    main()
