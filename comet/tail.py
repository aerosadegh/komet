from collections import deque
from sys import stdout
from time import sleep
from typing import Iterable

from .singleton import SimpleSingletonMeta, ThreadSafeSingletonMeta


class TailPrint(metaclass=ThreadSafeSingletonMeta):
    """
    A class for print python objects with tails.  implemented with singleton pattern.

    Args:
        max_count(int): Maximum count of lines to print.
        delay(float): Delay between prints of each line.
    """

    def __init__(self, max_count=5, delay=0.05) -> None:
        self.deq = deque(maxlen=max_count)
        self.delay = delay
        self.deq.append("")

    def _clear(self) -> None:
        """clear all previous lines from stdout."""
        for _ in range(len(self.deq)):
            stdout.write("\x1b[1A\x1b[2K")  # move up cursor and delete whole line

    def _print(self) -> None:
        """print all items in deque on stdout."""
        stdout.write("\n".join(self.deq) + "\n")  # print the lines
        sleep(self.delay)

    def __call__(self, *args: Iterable[str], sep: str = " ", end="\n") -> None:
        self._clear()
        self.deq.append(
            sep.join(map(lambda x: str(x), args))
        )  # remove first element and append new to the end
        self._print()


if __name__ == "__main__":
    # The client code.

    # First instance
    print1 = TailPrint(5)

    # TailPrint(7) is not created here and MetaClass return previous instance `TailPrint(5)`
    # This is Singleton!
    print2 = TailPrint(7)

    for i in range(50):
        if i % 2:
            print1(i)
        else:
            print2(i, i * 2, ":)", True)
