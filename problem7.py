__author__ = 'woorak'

from math import sqrt

N = 10001
n = 0

p=2
while n<N:
    while True:
        if p>1 and all(p % i for i in xrange(2, int(sqrt(p))+1)):
            n += 1
            p += 1
            break
        p += 1

print p-1