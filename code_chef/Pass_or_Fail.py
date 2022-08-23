# cook your dish here
T= int (input())
for i in range(T):
    N,X,P=map(int,input().split())
    incorrect=N-X
    passmark=(X*3)-((incorrect)*(1))
    
    if passmark>=P:
        print("PASS")
    
    else:
        print("FAIL")