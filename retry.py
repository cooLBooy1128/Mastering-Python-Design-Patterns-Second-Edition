import time
import sys
import os

FILENAME = 'data/file1.txt'


def create_file(filename, after_delay=5):
    time.sleep(after_delay)
    with open(filename, 'w') as f:
        f.write('A file creation test\n')


def append_data_to_file(filename):
    if os.path.exists(filename):
        with open(filename, 'a') as f:
            f.write('...Updating the file\n')
    else:
        raise OSError


if __name__ == '__main__':
    args = sys.argv
    # print(args)
    if args[1] == 'create':
        create_file(FILENAME)
        print(f"Created file '{FILENAME}'")
    elif args[1] == 'update':
        while True:
            try:
                append_data_to_file(FILENAME)
                print('Success! We are done!')
                break
            except OSError:
                print('Error... Try again')
