for _ in range(int(input())) :
    a,b = map(int,input().split())
    c = a-b
    if c > b:
        print(b)
    else:
        print(c)