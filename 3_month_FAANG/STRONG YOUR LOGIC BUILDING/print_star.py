# 1. Print single star https://drive.google.com/file/d/1hNQyIcGjoftFvCVsgn7g2o53n-ojkelT/view
print("*")

# 2. print 4 star
print("****")

# 3. Print n Star in same line
n = 5
for i in range(n):
    print("*", end="")

# 4. Print Square of Stars (n x n Stars)
n = 5
for i in range(n):
    for j in range(n):
        # print("\n",n)
        print("*", end="")
    print("\n")


# 5. Print an Increasing Triangle of Stars

print("5. Print an Increasing Triangle of Stars")
n = 5
for i in range(n):
    for j in range(i):
        print("*", end="")
    n += 1
    print("\n")
