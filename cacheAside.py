import sys
import sqlite3
import csv

cache_key_prefix = 'quote'


class QuoteCache:
    def __init__(self, filename=''):
        self.filename = filename

    def get(self, key):
        with open(self.filename) as csv_file:
            items = csv.reader(csv_file, delimiter=';')
            for item in items:
                if item[0] == key.split('.')[1]:
                    return item[1]

    def set(self, key, quote):
        existing = []
        with open(self.filename) as csv_file:
            items = csv.reader(csv_file, delimiter=';')
            existing = [cache_key_prefix + '.' + item[0] for item in items]
        if key in existing:
            print('This is weird. The key already exists.')
        else:
            with open(self.filename, 'a', newline='') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=['id', 'text'], delimiter=';')
                writer.writerow({'id': key.split('.')[1], 'text': quote})


def get_quote(quote_id):
    quote = cache.get(f'quote.{quote_id}')
    out = ''
    if quote is None:
        try:
            db = sqlite3.connect('data/quotes.sqlite3')
            cursor = db.cursor()
            cursor.execute(f'SELECT text FROM quotes WHERE id={quote_id}')
            for row in cursor:
                quote = row[0]
            out = f"GOT '{quote}' FROM DB"
        except Exception as e:
            print(e)
        finally:
            db.close()
        if quote is not None:
            key = f'{cache_key_prefix}.{quote_id}'
            cache.set(key, quote)
    else:
        out = f"{quote} (FROM CACHE, with key 'quote.{quote_id}')"
    return out


if __name__ == '__main__':
    args = sys.argv
    if args[1] == 'fetch':
        cache = QuoteCache('data/quotes_cache.csv')
        while True:
            quote_id = input('Enter the ID of the quote: ')
            q = get_quote(quote_id)
            if q:
                print(q)
