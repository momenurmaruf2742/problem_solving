# cook your dish here
from math import *
t = int(input())

for _ in range(t):
    x,y = map(int,input().split())
    ans = ceil((y-x)/8)
    print(ans)