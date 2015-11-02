__author__ = 'woorak'

print reduce(lambda a,b:a+b, filter(lambda x:x%3==0 or x%5==0, range(1000)))