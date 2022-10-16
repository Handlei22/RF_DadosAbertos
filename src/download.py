import threading
import time

import requests
import os
import glob
from tqdm import tqdm
from pathlib import Path

class Downloader(threading.Thread):
    def __init__(self, url, filename, parts_count=1):
        super().__init__()
        self.__parts = []
        self.__url = url
        self._filename = filename
        self.size = self.getSize()
        self.received = 0
        self.last_position = 0
        self.__parts_count = parts_count
        self.running = True

    def run(self):
        self.__get()

    def getSize(self):
        r = requests.head(self.__url)
        return int(r.headers.get('Content-Length'))

    def __get(self):
        r = requests.head(self.__url)
        self.size = int(r.headers.get('Content-Length'))
        count_thread = self.__parts_count
        nsize = self.size
        ncount = count_thread
        npos = 0

        for _ in range(0, count_thread):
            part_size = int(nsize / ncount)
            _p = _DownloadPart(self.__url, self._filename + '.part' + str(_), npos, part_size)
            self.__parts.append(_p)
            _p.download.start()
            nsize -= part_size
            ncount -= 1
            npos += part_size
        i = 0
        x = 0
        y = 0
        while True:
        # while sum([th.download.running for th in self.__parts]) < self.size:
            _received = 0
            for th in self.__parts:
                _p: _DownloadPart = th
                _received += _p.download.received
            self.received = _received

            if not any([th.download.running for th in self.__parts]):
            #     for th in self.__parts:
            #         _p: _DownloadPart = th
            #         _received += _p.download.received
            #     self.received = _received
                break

        for th in self.__parts:
            _p: _DownloadPart = th
            with open(self._filename, 'ab') as fs:
                with open(_p.filename, 'rb') as fp:
                    fs.write(fp.read())
                    fs.flush()
                    os.fsync(fs.fileno())

        self.removeFilesTmp()

        self.running = False

    def removeFilesTmp(self):
        for filename in glob.glob(f'{self._filename}.part*'):
            os.remove(filename)


class _DownloadPart:
    def __init__(self, url, filename, position, size):
        super().__init__()
        self.filename = filename
        self.position = position
        self.size = size
        self.download = Download(url, filename, headers={"Range": f'bytes={position}-{position + size - 1}'})


class Download(threading.Thread):
    def __init__(self, url, filename, headers):
        super().__init__()
        self.headers = headers
        self.__url = url
        self.size = 0
        self.received = 0
        self.running = True
        self.filename = filename
        self.getHeaderRange()


    def run(self):
        self.downloading()

    def downloading(self):
        headers = self.headers
        mode_file = 'wb'
        with requests.get(self.__url, stream=True, headers=headers) as r:
            Path(self.filename).parent.mkdir(parents=True, exist_ok=True)
            with open(f"{self.filename}", mode_file) as file:
                chunk_size = 8192
                for i, chunk in enumerate(r.iter_content(chunk_size=chunk_size)):
                    if chunk:
                        self.received += len(chunk)
                        file.write(chunk)
                        file.flush()
                        os.fsync(file.fileno())
                    time.sleep(0.1)
        self.running = False

    def getHeaderRange(self):
        if self.headers.get('Range'):
            _s = self.headers.get('Range')
            self.size = int(_s[_s.find('-') + 1:]) - int(_s[_s.find('=') + 1:_s.find('-')])

