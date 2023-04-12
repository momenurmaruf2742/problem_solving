for _ in range(int(input())):
    x,y,z = map(int,input().split())
    if z < y and z >= x:
        print("YES")
    else:
        print("NO")