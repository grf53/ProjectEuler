__author__ = 'woorak'

from math import sqrt

pfactors = {}

for n in range(21):
    p = 2
    while(p<=n):
        if n == 1:
            break
        if n%p==0:
            pn = 0
            while(n%p==0):
                n = int(n/p)
                pn += 1
            if not pfactors.has_key(p) or pn > pfactors[p]:
                pfactors[p] = pn
        p += 1
        while not (p>1 and all(p % i for i in xrange(2, int(sqrt(p))+1))):
            p += 1

prod = 1

for k in pfactors:
    for i in range(pfactors[k]):
        prod *= k

print prod