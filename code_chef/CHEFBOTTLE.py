# cook your dish here
for t in range(int(input())):
    n,x,k=map(int,input().split())
    if k/x>=n:
        print(n)
    else:
        print(k//x)