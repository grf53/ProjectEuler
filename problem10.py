__author__ = 'woorak'

from time import time
from math import sqrt

N = 2000000
sum = 0

p=2
while p<N:
    while True:
        if p>1 and all(p % i for i in xrange(2, int(sqrt(p))+1)):
            sum += p
            p += 1
            break
        p += 1

print sum - (p - 1)