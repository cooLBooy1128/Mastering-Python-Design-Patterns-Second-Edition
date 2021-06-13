import contextlib
import io
from rx.core import Observer
from rx import create, operators
import rx


# Example 1
class ZenQuotesObserver(Observer):
    def on_next(self, value):
        print(f'Received: {value}')

    def on_completed(self):
        print('Done!!!')

    def on_error(self, error):
        print(f'Error Occurred: {error}')


def get_quotes():
    zen = io.StringIO()
    # print(zen.getvalue())
    with contextlib.redirect_stdout(zen):
        import this
    quotes = zen.getvalue().split('\n')[2:-1]
    # print(quotes)
    return quotes


def push_quotes(obs, sch):
    quotes = get_quotes()
    for q in quotes:
        if q:
            obs.on_next(q)
    obs.on_completed()


def main1():
    source = create(push_quotes)
    source.subscribe(ZenQuotesObserver())


# Example 2
def get_quotes_enum():
    zen = io.StringIO()
    with contextlib.redirect_stdout(zen):
        import this
    quotes = zen.getvalue().split('\n')[1:]
    return enumerate(quotes)


if __name__ == '__main__':
    # main1()

    zen_quotes = get_quotes_enum()
    rx.from_(zen_quotes).pipe(operators.filter(lambda q: len(q[1]) > 0)).subscribe(
        lambda q: print(f'Received: {q[0]} - {q[1]}'))
