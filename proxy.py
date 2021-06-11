from abc import ABCMeta, abstractmethod


# virtual proxy
class LazyProperty:
    def __init__(self, method):
        self.method = method
        self.method_name = method.__name__
        # print(f'function overriden: {self.method}')
        # print(f'function name: {self.method_name}')

    def __get__(self, instance, owner):
        print(f'{self = }, {instance = }, {owner = }')
        if not instance:
            return None
        value = self.method(instance)
        print(f'value: {value}')
        setattr(instance, self.method_name, value)
        return value


class Test:
    def __init__(self):
        self.x = 'foo'
        self.y = 'bar'
        self._resource = None

    @LazyProperty
    def resource(self):
        print(f'initializing self._resource which is: {self._resource}')
        self._resource = tuple(range(5))
        return self._resource


def main1():
    t = Test()
    print(f'{t.__dict__ = }')
    print(t.x)
    print(t.y)
    print(t.resource)
    print(f'{t.__dict__ = }')
    print(t.resource)


# protection proxy
class SensitiveInfo(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        self.users = ['nick', 'tom', 'ben', 'mike']

    def read(self):
        nb = len(self.users)
        print(f"There are {nb} users: {' '.join(self.users)}")

    def add(self, user):
        self.users.append(user)
        print(f'Added user {user}')

    def remove(self, user):
        self.users.remove(user)
        print(f'Removed user {user}')


class Info(SensitiveInfo):
    def __init__(self):
        super().__init__()
        self.secret = '123qwe'

    def add(self, user):
        sec = input('what is the secret? ')
        super().add(user) if sec == self.secret else print('That is wrong!')

    def remove(self, user):
        sec = input('what is the secret? ')
        try:
            super().remove(user) if sec == self.secret else print('The secret is wrong!')
        except ValueError:
            print(f"User {user} doesn't exist")


def main2():
    info = Info()
    while True:
        print('1. read list || 2. add user || 3. delete user || 4. quit')
        key = input('choose option: ')
        if key == '1':
            info.read()
        elif key == '2':
            name = input('choose username: ')
            info.add(name)
        elif key == '3':
            name = input('choose username: ')
            info.remove(name)
        elif key == '4':
            exit()
        else:
            print(f'unknown option: {key}')


if __name__ == '__main__':
    # main1()
    main2()
