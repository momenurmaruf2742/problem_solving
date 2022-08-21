itret_number=int(input())
for st in range(itret_number):
    st_p=input()
    if len(st_p)>10:
        s=st_p
        s1=s[0]
        sl=s[-1]
        sm=s[1 :-1]
        print(s1+str(len(sm))+sl)
    else:
        print(st_p)




