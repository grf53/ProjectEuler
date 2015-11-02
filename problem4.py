__author__ = 'woorak'


def make_palindrome(former):
    latter = int(str(former)[::-1])
    return former*1000 + latter

def is_prod_of_hundreds(n):
    for i in range(100,1000):
        q,r = divmod(n, i)
        if r == 0 and 999 >= q >= 100:
            return True

half = 997 # 998899 > 999*999 > 997799

while(half>0):
    palin = make_palindrome(half)
    if is_prod_of_hundreds(palin):
        print palin
        break
    half -= 1