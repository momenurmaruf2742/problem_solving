for _ in range(int(input())):
    a,b,c = map(int,input().split())
    second_max = sorted([a, b, c])[1]
    print(second_max)
    # if a>b>c or c>b>a:
    #     print(b)
    # elif b>c>a or a>c>b:
    #     print(c)
    # else:
    #     print(a)