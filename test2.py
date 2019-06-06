import random
import time


def rand(n, upper):
    start = time.time()
    randnum = random.randint(1000, upper)
    while n != randnum:
        randnum = random.randint(1000, upper)
    return time.time() - start


def step(n):
    start = time.time()
    stepnum = 1000
    while n != stepnum:
        stepnum = stepnum + 1
    return time.time() - start
