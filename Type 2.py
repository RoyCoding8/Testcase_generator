"""
Format:
    t
    n

    a1 a2 ... an
"""


import random as rn

lt=int(input("Enter lower bound for t: "))
ut=int(input("Enter upper bound for t: "))

ln=int(input("Enter lower bound for n: "))
un=int(input("Enter upper bound for n: "))

la=int(input("Enter lower bound for ai: "))
ua=int(input("Enter upper bound for ai: "))

t=rn.randrange(lt,ut+1)
print(t)

for _ in range(t):
    n=rn.randrange(ln,un+1)
    a=rn.sample(range(la,ua+1),n)
    print(n)
    print(*a)