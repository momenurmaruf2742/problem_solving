n = int(input()) # input number of statements
x = 0
for i in range(n):
    statement = input() # input statement
    if "++" in statement:
        x += 1
    elif "--" in statement:
        x -= 1
print(x)