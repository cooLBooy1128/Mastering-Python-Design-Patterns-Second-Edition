import os

verbose = True


class RenameFile:
    def __init__(self, src, desc):
        self.src = src
        self.desc = desc

    def execute(self):
        if verbose:
            print(f"[renaming '{self.src}' to '{self.desc}']")
        os.rename(self.src, self.desc)

    def undo(self):
        if verbose:
            print(f"[renaming '{self.desc}' to '{self.src}']")
        os.rename(self.desc, self.src)


class CreateFile:
    def __init__(self, path, txt='hello world\n'):
        self.path = path
        self.txt = txt

    def execute(self):
        if verbose:
            print(f"[creating file '{self.path}']")
        with open(self.path, 'w', encoding='utf8') as f:
            f.write(self.txt)

    def undo(self):
        delete_file(self.path)


class ReadFile:
    def __init__(self, path):
        self.path = path

    def execute(self):
        if verbose:
            print(f"[reading file '{self.path}']")
        with open(self.path, 'r', encoding='utf8') as f:
            print(f.read(), end='')


def delete_file(path):
    if verbose:
        print(f'deleting file {path}')
    os.remove(path)


def main():
    orig_name, new_name = 'data/file1', 'data/file2'
    commands = (CreateFile(orig_name),
                ReadFile(orig_name),
                RenameFile(orig_name, new_name))
    [c.execute() for c in commands]

    answer = input('undo the executed commands? [y/n] ')
    if answer not in ('y', 'Y'):
        print(f'the result is {new_name}')
        exit()
    for c in reversed(commands):
        try:
            c.undo()
        except AttributeError as e:
            print('Error:', str(e))


if __name__ == '__main__':
    main()
