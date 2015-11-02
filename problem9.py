__author__ = 'woorak'

"""
m,n in N
let
a = m**2 + 2*m*n
b = 2*m*n + 2* n**2
c = m**2 + 2*m*n + 2* n**2
=> a, b, c : pithagorean triple
"""

def routine():
    N = 0
    while True:
        for m in range(1,N):
            n = N-m
            a = m**2 + 2*m*n
            b = 2*m*n + 2* n**2
            c = m**2 + 2*m*n + 2* n**2
            s = a+b+c
            if 1000%s == 0:
                return a*b*c*((1000/s)**3)
        N += 1

print routine()



