import pyfiglet
from src.config import PROGRAM_NAME, AUTHOR, VERSION
from colorama import Fore


def banner():
    print('\033[2J')
    custom_fig = pyfiglet.Figlet(font='small')
    print(f'{Fore.RED}{custom_fig.renderText(PROGRAM_NAME)}')
    print('\033[2A')
    print(f'{Fore.YELLOW}Author: {AUTHOR}')
    print(f'{Fore.YELLOW}Version: {VERSION}')
    print('\n[!] CNPJ DOWNLOADER is a script to assist in downloading the entire CNPJ structure provided by RECEITA FEDERAL.')
    print('\n--------------------------------------------------------------------\n\n')