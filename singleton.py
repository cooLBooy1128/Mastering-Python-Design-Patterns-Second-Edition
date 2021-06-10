import urllib.request
import urllib.parse


class SingletonType(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        # print(cls)
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class URLFetcher(metaclass=SingletonType):
    def __init__(self):
        self.urls = []
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'
        }

    def fetch(self, url):
        req = urllib.request.Request(url, headers=self.headers)
        with urllib.request.urlopen(req) as response:
            if response.code == 200:
                page = response.read()
                print(page)
                self.urls.append(url)

    def dump_url_registry(self):
        return ', '.join(self.urls)


def main():
    MY_URLS = ['http://www.voidspace.org.uk',
               'http://google.com',
               'https://www.youtube.com',
               'http://python.org',
               'https://www.python.org/error']
    print(URLFetcher() is URLFetcher())
    fetcher = URLFetcher()
    for url in MY_URLS:
        try:
            fetcher.fetch(url)
        except Exception as e:
            print(e)
    print('-'*20)
    done_urls = fetcher.dump_url_registry()
    print(f'Done URLs: {done_urls}')


if __name__ == '__main__':
    main()
