import colorama
import os
from download import Downloader

colorama.init()


def main():
    d = Downloader('http://200.152.38.155/CNPJ/Socios9.zip', f'{os.path.dirname(os.path.realpath(__file__)) + os.sep}files{os.sep}Socios9.zip', 100)
    d.start()

    while d.running:
        print(f'\r{int(d.size / 1024)}/{int(d.received / 1024)}', end='')
    print('End.')


if __name__ == '__main__':
    main()
