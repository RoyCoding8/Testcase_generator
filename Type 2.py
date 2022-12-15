"""
Format:
    t
    n
    a1 a2 ... an
"""

import random as rn

ln=int(input("Enter lower bound for t: "))
un=int(input("Enter upper bound for t: "))
lm=int(input("Enter lower bound for n: "))
um=int(input("Enter upper bound for n: "))
la=int(input("Enter lower bound for ai: "))
ua=int(input("Enter upper bound for ai: "))
t=rn.randrange(ln,un+1)
n=rn.randrange(lm,um+1)
a=rn.sample(range(la,ua+1),n)
for _ in range(t):
    print(n)
    print(*a)