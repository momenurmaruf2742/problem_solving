T = int(input())

# Loop through each test case and solve
for i in range(T):
    N,A,B,C = map(int, input().split())  # Input two integers X and Y
    if A+C>=N:
        if B//2>=A or B//2>=C:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")