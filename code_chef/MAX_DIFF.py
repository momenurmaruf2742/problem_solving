for _ in range(int(input())):
    n,s=map(int,input().split())
    if s<n:
        ans = s
    else:
        ans = n*2-s
    print(ans)