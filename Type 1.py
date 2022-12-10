"""
Format:
    n m
    a1 a2 ... an
"""

import random as rn

ln=int(input("Enter lowexier bound for n: "))
un=int(input("Enter upper bound for n: "))
lm=int(input("Enter lower bound for m: "))
um=int(input("Enter upper bound for m: "))
la=int(input("Enter lower bound for ai: "))
ua=int(input("Enter upper bound for ai: "))
n=rn.randrange(ln,un+1)
m=rn.randrange(lm,um+1)
a=rn.sample(range(la,ua+1),n)
print(n,m)
print(*a)