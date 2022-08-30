# cook your dish here
t = int(input())
for i in range(t):
    a,b=map(int,input().split())
    c,d=map(int,input().split())
    if a<=c and b<=d:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")