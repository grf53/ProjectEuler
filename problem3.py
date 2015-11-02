__author__ = 'woorak'

from math import sqrt

N = 600851475143
pfactors = []
p = 2
n = N

while(p <= N):
    if n == 1:
        break
    if n%p==0:
        pfactors.append(p)
        while(n%p==0):
            n = int(n/p)
    p += 1
    while not (p>1 and all(p % i for i in xrange(2, int(sqrt(p))+1))):
        p += 1

print(pfactors[-1])
