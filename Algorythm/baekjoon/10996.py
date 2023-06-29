n = int(input())

if n == 1 :
    print('*')

else:
    for i in range(1, 2*n+1):
        if n % 2 == 0:
            if i % 2 == 1:
                print('* '*int(n/2))
            else:
                print(' *'*int(n/2))

        else :
            if i % 2 == 1:
                print('* '*int((n+1)/2))
            else:
                print(' *'*int((n-1)/2))