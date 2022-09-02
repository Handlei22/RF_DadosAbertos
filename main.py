import sys
import time
import colorama
from colorama import Fore, Back, Style
import random
import os
import requests
import shutil
from tqdm.auto import tqdm
from bs4 import BeautifulSoup
from download import Downloader

colorama.init()


def main():
    d = Downloader('http://200.152.38.155/CNPJ/LAYOUT_DADOS_ABERTOS_CNPJ.pdf',  f'{os.path.dirname(os.path.realpath(__file__))+os.sep}files{os.sep}S.pdf', 4)
    d.start()

    while d.running:
        print(f'\r{int(d.size/1024)}/{int(d.received/1024)}', end='')
    print('fim')


    # listfiles = []
    # r = requests.get('http://200.152.38.155/CNPJ')
    # soup = BeautifulSoup(r.text, 'html.parser')
    # table = soup.find('table')
    # rows = table.find_all('tr')[1::]
    # for row in rows:
    #     cols = row.find_all('td')
    #     if cols:
    #         if cols[1].text.strip().find('.zip') > 0:
    #             listfiles.append(f'http://200.152.38.155/CNPJ/{cols[1].text.strip()}')
    #             # print(f'{cols[1].text.strip()} - {cols[3].text.strip()}')
    # listThreads = []
    # p = Proxys()
    # if listfiles:
    #     for url in listfiles:
    #         th = Download(url, p)
    #         listThreads.append(th)
    #
    # for th in listThreads:
    #     th.start()
    #     time.sleep(2.5)
    #
    # while any([ th.running for th in listThreads ]):
    #     for _index, th in enumerate(listThreads):
    #         print(f'\r\033[500D\033[1B{str(_index).zfill(3)}: {str(int((th.position*100)/int(th.size))).zfill(3)}%  {int((th.position/1024)/1024)}/{int((th.size/1024)/1024)} -- {int(th.speed/1024)}Kb/s - Alive: {th.running} | {th.filename}', end='')
    #         time.sleep(.2)
    #     time.sleep(3)
    #     print(f'\033[{len(listThreads)+1}A')
    #     # time.sleep(5)





    # d = Download('http://200.152.38.155/CNPJ/Socios4.zip')
    # d.start()
    # while d.running:
    #     print(f'\r{int(d.position/1024)}/{d.size/1024} -- {d.speed}Kb/s', end='')
    #     time.sleep(1)
    # print('terminado')



def create_blocks(aCount, atype):
    if atype == 1:
        return '\033[43m  \033[0m '*int(aCount)
    elif atype == 2:
        return '\033[43m   \033[0m'*int(aCount)

# def main():
#     vList = []
#     for d in range(1, 50):
#         vList.append(
#             {'name': f'T{str(d).zfill(3)}', 'total': 0, 'cnpj': 0, 'ie': 0, 'proxy': 0, 'ativa': 'sim'}
#         )
#
#     while True:
#         p = 0
#         _thread = f'\033[1B{Fore.RED}Thread: '
#         _cnpj = f'\033[1B{Fore.RED}CNPJ:   '
#         _ie = f'\033[1B{Fore.RED}IE:     '
#         _proxy = f'\033[1B{Fore.RED}Proxy:  '
#         _ativo = f'\033[1B{Fore.RED}Ativo:  '
#         _total = f'\033[1B{Fore.RED}Total:  '
#
#         _p = 3
#
#         for _, item in enumerate(vList):
#             item['total'] += random.randint(0, 10)
#             item['cnpj'] += random.randint(0, 100)
#             item['ie'] += random.randint(0, 100)
#             item['proxy'] += random.randint(0, 100)
#             if item['total'] > 100:
#                 item['total'] = 100
#
#             _thread += f'\033[{_p}C{item["name"]}'
#             _cnpj += f'\033[{_p}C{str(item["cnpj"]).zfill(4)}'
#             _ie += f'\033[{_p}C{str(item["ie"]).zfill(4)}'
#             _proxy += f'\033[{_p}C{str(item["proxy"]).zfill(4)}'
#             _ativo += f'\033[{_p}C{item["ativa"]} '
#             _total += f'\033[{_p}C{str(item["total"]).zfill(3)}%'
#             s = '' #create_blocks(item['total'] / 4, 1)
#
#         print(f'\r{_thread}', end='')
#         print(f'\r{_cnpj}', end='')
#         print(f'\r{_ie}', end='')
#         print(f'\r{_proxy}', end='')
#         print(f'\r{_ativo}', end='')
#         print(f'\r{_total}', end='')
#
#         time.sleep(1.5)
#
#
#         print('\033[6A', end='')
#         print(f'\033[{_p+2}D', end='')
#         if all(item['total'] == 100 for item in vList):
#             break

# def main():
#     vList = []
#     for d in range(1, 15):
#         vList.append({'name': f'T{str(d).zfill(3)}', 'total': 0})
#
#     while True:
#         for item in vList:
#             item['total'] += random.randint(0, 10)
#             if item['total'] > 100:
#                 item['total'] = 100
#
#             s = create_blocks(item['total']/4, 1)
#             print(f'\r\033[1B{Fore.RED}{item["name"]}: \033[0m{s} \033[{75-int(item["total"]/4)-(int(item["total"]/4)*2)}C\033[33m{str(item["total"]).zfill(3)} %\033[0m', end='')
#             # time.sleep(0.1)
#         print('')
#         for item in vList:
#             s = create_blocks(item['total']/4, 2)
#             print(f'\r\033[1B{Fore.RED}{item["name"]}: \033[0m{s} \033[{75-int(item["total"]/4)-(int(item["total"]/4)*2)}C\033[33m{str(item["total"]).zfill(3)} %\033[0m', end='')
#
#         time.sleep(0.2)
#
#         if all(item['total'] == 100 for item in vList):
#             break
#         print(f'\033[{len(vList)*2+2}A')


# def main():
#     vList = []
#     for d in range(1, 15):
#         vList.append({'name': f'T{str(d).zfill(3)}', 'total': 0})
#
#     while True:
#         for item in vList:
#             item['total'] += random.randint(0, 10)
#             if item['total'] > 100:
#                 item['total'] = 100
#
#             s = create_blocks(item['total']/4, 1)
#             print(f'\r\033[1B{Fore.RED}{item["name"]}: \033[0m{s} \033[{75-int(item["total"]/4)-(int(item["total"]/4)*2)}C\033[33m{str(item["total"]).zfill(3)} %\033[0m', end='')
#             # time.sleep(0.1)
#         print('')
#         for item in vList:
#             s = create_blocks(item['total']/4, 2)
#             print(f'\r\033[1B{Fore.RED}{item["name"]}: \033[0m{s} \033[{75-int(item["total"]/4)-(int(item["total"]/4)*2)}C\033[33m{str(item["total"]).zfill(3)} %\033[0m', end='')
#
#         time.sleep(0.2)
#
#         if all(item['total'] == 100 for item in vList):
#             break
#         print(f'\033[{len(vList)*2+2}A')



if __name__ == '__main__':
    main()
