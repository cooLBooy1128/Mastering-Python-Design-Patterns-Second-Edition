import urllib.request
from abc import ABCMeta, abstractmethod


class ResourceContentFetcher(metaclass=ABCMeta):
    @abstractmethod
    def fetch(self, path):
        pass


class URLFetcher(ResourceContentFetcher):
    def fetch(self, path):
        req = urllib.request.Request(path)
        with urllib.request.urlopen(req) as response:
            if response.code == 200:
                page = response.read()
                print(page)


class LocalFileFetcher(ResourceContentFetcher):
    def fetch(self, path):
        with open(path) as f:
            content = f.read()
            print(content)


class ResourceContent:
    def __init__(self, fetcher):
        self._fetcher = fetcher

    def show_content(self, path):
        self._fetcher.fetch(path)


def main():
    url_fetcher = URLFetcher()
    iface = ResourceContent(url_fetcher)
    iface.show_content('https://www.python.org/')
    print('=' * 50)
    local_fetcher = LocalFileFetcher()
    iface = ResourceContent(local_fetcher)
    iface.show_content('README.md')


if __name__ == '__main__':
    main()
