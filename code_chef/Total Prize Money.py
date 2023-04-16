# for i in range(int(input())):
#     a,b = map(int,input().split())
#     sum1=0
#     sum2=0
#     for _ in range(1,10+1):
#         sum1 += a
#     for _ in range(11,100+1):
#         sum2 += b
#     print(sum1+sum2)
    


T = int(input())

# Loop through each test case and solve
for i in range(T):
    X, Y = map(int, input().split()) # Input two integers X and Y
    
    # Calculate total prize money
    total_prize_money = 10 * X + 90 * Y
    print(total_prize_money)