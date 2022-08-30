# cook your dish here
t = int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    if x+z>y:
        print("NO")
    else:
        print("YES")
    
