__author__ = 'woorak'

fibo = [1,2]

i=1
while fibo[i]<4000000:
    i += 1
    fibo.append(fibo[i-1]+fibo[i-2])

print reduce(lambda a,b:a+b, filter(lambda x:x%2==0, fibo))