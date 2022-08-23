# cook your dish here
t=int(input())
for i in range(t):
    n = int (input())
    count=1
    for j in range(1,n+1):
        count*=j
    print(count)