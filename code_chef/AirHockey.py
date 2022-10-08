for _ in range (int(input())):
    a,b=map(int,input().split())
    if a>b or a==b:
        print(7-a)
    elif b>a:
        print(7-b)
    elif a==0 and b==0:
        print("7")
        