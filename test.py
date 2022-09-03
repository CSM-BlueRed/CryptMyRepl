# This is a example file
# try to make a private repl with this command:
# ---------------------------
#
# python -m CryptMyRepl "./test.py"
#
# ---------------------------
# follow the instructions and done!

from typing import Iterable, Iterator, Any



class Infiniterator:

    def __init__(self, iterable: Iterable) -> None:
        self.iterable: Iterable = tuple(iterable)
        self._index: int = 0


    def __iter__(self) -> Iterator:
        yield from self.iterable

    
    def __len__(self) -> int:
        return len(self.iterable)

    
    def __next__(self) -> Any:
        self._index += 1

        if len(self) <= (self._index - 1):
            self._index = 1

        n = list(self)[self._index - 1]
        return n

    
    def seek(self, offset: int) -> None:
        if offset >= len(self):
            raise ValueError(f'offset cannot be equal or > of len(self)')
        self._index = offset


    def __mod__(self, other: int) -> Iterator:
        new = self.__class__(self)
        n = []

        for _ in range(other):
            n.append(next(new))
        yield from n



abc: Infiniterator = Infiniterator('ABC')
count: int = 9
new: Iterator = list(abc % 9)

print('    '.join(new))
print('    '.join('^' * count))
print('    '.join('123456789'))
input()