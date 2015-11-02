__author__ = 'woorak'

l = range(1, 101)
s = lambda a,b:a+b
q = lambda x:x**2
r = reduce

print abs(q(r(s,l))-r(s,map(q,l)))