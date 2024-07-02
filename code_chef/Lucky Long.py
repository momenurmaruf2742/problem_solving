for _ in range(int(input())):
    s = input().strip()
    count = 0
    for char in s:
        if char != '4' and char != '7':
            count += 1
    print(count)