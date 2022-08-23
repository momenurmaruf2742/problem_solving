# cook your dish here
moneyHave=int(input())
apple,orrange=map(int,input().split())

if (apple+orrange)<=moneyHave:
    print("Yes")
else:
    print("No")