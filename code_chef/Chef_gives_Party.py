for _ in range (int(input())):
    n,x,k=map(int,input().split())
    if n*x<=k:
        print("YES")
    else:
        print("NO")