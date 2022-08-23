# cook your dish here
t=int(input())

for i in range(t):
    count=0
    input_problem=int(input())
    array=list(map(int,input().split()))
    for j in range(len(array)):
        
        if array[j]>=1000:
            count+=1
    print(count)