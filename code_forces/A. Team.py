count=0

for i in range(0,int(input())):
    x=input()
    if x.count('1')>=2:
        count+=1
print(count)