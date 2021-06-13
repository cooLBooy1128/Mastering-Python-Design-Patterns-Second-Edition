import contextlib
import io
import rx
from rx import operators as ops


def get_quotes_enum():
    zen = io.StringIO()
    with contextlib.redirect_stdout(zen):
        import this
    quotes = zen.getvalue().split('\n')[1:]
    return enumerate(quotes)


def my_filter():
    return rx.pipe(
        ops.flat_map(lambda seq: rx.from_(zen_quotes)),
        ops.flat_map(lambda q: rx.from_(q[1].split())),
        ops.filter(lambda s: len(s) > 2),
        ops.map(lambda s: s.replace('.', '').replace(',', '').replace('!', '').replace('-', '').lower())
    )


if __name__ == '__main__':
    zen_quotes = list(get_quotes_enum())
    rx.interval(2).pipe(my_filter()).subscribe(lambda s: print(f'Received: {s}'))
    input("Press any key to exit\n")
