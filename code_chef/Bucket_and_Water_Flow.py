# cook your dish here
t=int(input())
for i in range(t):
    w,x,y,z=map(int,input().split())
    
    cal=y*z+w
    if cal>x:
        print("overflow")
    elif cal==x:
        print("filled")
    else:
        print("unfilled")