from test2 import *
import numpy as np

if __name__ == '__main__':
    upper = 99999
    code = int(input('Enter value between 1000 and %d : ' % upper))
    if 1000 > code or code > upper:
        print('Invalid code')
        exit(1)

    rand_time = 0.0
    step_time = 0.0
    num_test = 5
    for i in range(num_test):
        rand_time += rand(code, upper)
        step_time += step(code)

    print('Random time solver: %f' % (rand_time/num_test))
    print('Step time solver: %f' % (step_time/num_test))
