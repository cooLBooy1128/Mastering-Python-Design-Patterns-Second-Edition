import time
from datetime import datetime
import random

import pybreaker

breaker = pybreaker.CircuitBreaker(fail_max=3, reset_timeout=7)


@breaker
def fragile_function():
    if not random.choice([True, False]):
        print(' / OK', end='')
    else:
        print(' / FAIL', end='')
        raise Exception('This is a sample Exception')


def main():
    while True:
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), end='')
        try:
            fragile_function()
        except Exception as e:
            print(f' / {type(e)} {e}', end='')
        finally:
            print()
            time.sleep(1)


if __name__ == '__main__':
    main()
