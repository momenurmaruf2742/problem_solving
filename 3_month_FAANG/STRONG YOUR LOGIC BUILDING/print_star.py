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
    print()
     # another version
n = 5
print("another version")
for i in range(1,n+1):
    print("*" * i)

# 6. Print a Right-Aligned Triangle of Stars
print("6. Print a Right-Aligned Triangle of Stars")
n = 5
for i in range(1,n+1):
     for j in range(n-i):
         print(" ",end="")
     for k in range(i):
         print("*", end="")
     print()

     # another version
print("another version")
for i in range(1,n+1):
    print(" " * (n-i) + "*" * i)

# 7. Print Stars in Even Numbers (2, 4, 6, 8, 10)
print("7. Print Stars in Even Numbers (2, 4, 6, 8, 10)")
for i in range(2,11,2):
    print("*" * i)

# 8. Print Stars in Odd Numbers (1, 3, 5, 7, 9)
print("8. Print Stars in Odd Numbers (1, 3, 5, 7, 9)")
for i in range(1,10,2):
    print("*" * i)

# 9. Print a Centered Pyramid of Stars
print("9. Print a Centered Pyramid of Stars")
n = 5
for i in range(n):
    for j in range(n - i - 1):
        print(" ",end="")
    for k in range(2*i+1):
        print("*",end="")
    print()
    #  another way
print("another version")
n = 5
for i in range(n):
    print(" " * (n-i-1) + "*" * (2*i+1))


# 10. Print Stars and Spaces Alternating (Stars and Blank Spaces)
print("10. Print Stars and Spaces Alternating (Stars and Blank Spaces)")
n = 5

for i in range(n):
    # Print leading characters
    for j in range(n - i - 1):
        print("B", end="")

    # Print alternating stars and spaces
    for j in range(2 * i + 1):
        if j % 2 == 0:
            print("*", end="")
        else:
            print("B", end="")

    print()

# 11. Print Numbers in an Increasing Sequence (1, 12, 123, 1234, 12345)
print("11. Print Numbers in an Increasing Sequence (1, 12, 123, 1234, 12345)")
n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end="")
    print()