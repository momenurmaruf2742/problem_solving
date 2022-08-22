# cook your dish here
n = int (input())

for i in range(n):
    a,b,c=map(int,input().split())
    
    if a>=b and a>=c:
        if b>=c:
            print(b)
        else:
            print(c)
    elif b>=c and b>=a:
        if c>=a:
            print(c)
        else:
            print(a)
    else:
        if a>=b:
            print(a)
        else:
            print(b)