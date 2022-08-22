# cook your dish here

N = int(input())
count1=0
count2=0

wepon = list(map(int,input().strip().split()))[:N]


for j in range(len(wepon)):
    if wepon[j]%2==0:
        count1+=1
    else:
        count2+=1 
if count1>count2:
    print("READY FOR BATTLE")
elif count1==count2:
    print("NOT READY")
else:
    print("NOT READY")