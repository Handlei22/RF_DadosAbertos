import sys


class ProgressBar:
    def __init__(self, size, desc='', out=sys.stdout):
        self.min = 0
        self.max = 100
        self.size = size
        self.position = 0
        self.percentage = 0
        self.__desc = desc
        self.out = out
        self.string = self.__mountBarStr(0)

    @property
    def desc(self):
        return self.__desc

    @desc.setter
    def desc(self, value):
        self.__desc = str(value)

    def update(self, _position):
        self.position = _position
        percent = int((_position * 100) / self.size)
        if percent <= self.percentage:
            return
        self.string = self.__mountBarStr(percent)
        self.percentage = percent

    def __mountBarStr(self, percent):
        return str(f'\r{str(percent).zfill(3)}%|\033[43m{" " * percent}\033[0m\033[33m{"." * (100 - percent)}\033[0m|{self.desc}')
