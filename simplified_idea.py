from collections import deque
from random import choices, randint
from string import ascii_letters
from sys import stdout
from time import sleep

deq = deque(maxlen=5)
delay = 0.15
sep = " "


def get_random_items(num):
    n = randint(2, 10)
    return [num, *choices(ascii_letters, k=n)]


args_list = [get_random_items(i) for i in range(50)]

for args in args_list:
    # clear last print lines
    for _ in range(len(deq)):
        stdout.write("\x1b[1A\x1b[2K")  # move up cursor and delete whole line

    # prepare new lines
    deq.append(
        sep.join(map(lambda x: str(x), args))
    )  # remove first element and append new to the end

    # re-print the lines
    stdout.write("\n".join(deq) + "\n")
    sleep(delay)
