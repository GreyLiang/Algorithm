import os
import cmath

n = list(input())
print(n)
def minn(n):
    mi = []
    n.sort()
    for i in range(len(n)):
        mi.append(int(n[i]))
    return mi
def maxn(n):
    ma = [0]*len(n)
    n.sort(reverse=True)
    for i in range(len(n)):
        ma.append(int(n[i]))
    return ma

def fun(ma,mi):
    t = (ma[0]*1000+ma[1]*100+ma[2]*10+ma[3])-(mi[0]*1000+mi[1]*100+mi[2]*10+mi[3])
    return t

def lists(s):
    return list(str(s))

while True:
    a = maxn(n)
    b = minn(n)
    c = fun(a,b)
    if c == 6174:
        print("It is OK...")
        break
    else:
        n = lists(c)