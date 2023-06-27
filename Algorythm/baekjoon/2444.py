n = int(input())

for i in range(2*n-1):
    

    if i < n:
        x = (n-i-1)
        print(" "*x, end = '')
        print("*"*(1+2*i))
    else :
        x = (i-n+1)
        print(" "*x, end = '')
        print("*"*(2*(n-x) - 1))
