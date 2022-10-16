import colorama
import os
from src.download import Downloader
import requests
from bs4 import BeautifulSoup
import time
import ctypes
import cursor
from src.progress_bar import ProgressBar
from src import banner

colorama.init(autoreset=True)


def main():
    banner.banner()
    input('s')

    cursor.hide()
    __quickedit(0)

    url = 'http://200.152.38.155/CNPJ'
    listfiles = []
    list_threads = []
    count_th = 50

    print(f'requisitando dados em: {url}')
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    table = soup.find('table')
    rows = table.find_all('tr')[1::]
    print(f'\rBuscando arquivos pra serem baixados...', end='')
    _c = 0
    for row in rows:
        cols = row.find_all('td')
        if cols:
            if cols[1].text.strip().find('.zip') > 0:
                _c += 1
                listfiles.append(f'http://200.152.38.155/CNPJ/{cols[1].text.strip()}')
                print(f'\rBuscando arquivos pra serem baixados: {_c}', end='')
        if _c == 5:
            break
    print(f'\n{_c} arquivos encontrado.')
    print(f'\rCriando threads de download...', end='')
    for _, url in enumerate(listfiles):
        print(f'{os.path.dirname(os.path.realpath(__file__)) + os.sep}'
        f'{os.path.basename(url).replace(".zip", "")}'
        f'{os.sep}'
        f'{os.path.basename(url)}')
        d = Downloader(url,
                       f'{os.path.dirname(os.path.realpath(__file__)) + os.sep}downloads{os.sep}'
                       f'{os.path.basename(url).replace(".zip", "")}'
                       f'{os.sep}'
                       f'{os.path.basename(url)}',
                       count_th
        )
        print(f'\rCriando threads de download... {_+1}/{len(listfiles)}', end='')
        # print('\033[1B', end='')
        list_threads.append({'th': d, 'progress': ProgressBar(d.size, desc=os.path.basename(url))})
    # print(f'\033[{len(list_threads)}A', end='')
    print(f'\n{len(listfiles)} threads criadas.')

    print(f'\rIniciando threads...', end='')
    for _, item in enumerate(list_threads):
        print(f'\rIniciando threads... {_ + 1}/{len(list_threads)}', end='')
        item['th'].start()
        time.sleep(1)
    print(f'\n{len(listfiles)} threads iniciadas.')

    while any([item['th'].running for item in list_threads]):
        for item in list_threads:
            item['progress'].update(item['th'].received)
            print(f'{item["progress"].string}', end='')
            print('\033[1B', end='')
        print(f'\033[{len(list_threads)}A', end='')
        time.sleep(1)


    cursor.show()
    __quickedit(1)

def __quickedit(enabled=1):
    kernel32 = ctypes.windll.kernel32
    if enabled:
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), (0x4 | 0x80 | 0x20 | 0x2 | 0x10 | 0x1 | 0x40 | 0x100))
    else:
        kernel32.SetConsoleMode(kernel32.GetStdHandle(-10), (0x4 | 0x80 | 0x20 | 0x2 | 0x10 | 0x1 | 0x00 | 0x100))

if __name__ == '__main__':
    main()
