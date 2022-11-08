
total = 0

n, k = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(n):
    if arr[i] >= arr[k - 1] and arr[i] > 0:
        total += 1

print(total)