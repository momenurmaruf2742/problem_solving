for i in range(int(input())):
    uc=0
    try:
        n = int(input())
        for _ in range(n):
            s = input()
            if s.upper()=="U":
                uc+=1
        if uc % 2 == 1:
            print("YES")
        else:
            print("NO")
    except EOFError as e:
        print(e)