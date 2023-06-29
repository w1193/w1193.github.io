n = int(input())

for i in range(1,2*n):
    x = i - n
# i <= n
    if i < n :

    #블링크 i-1개
        print(' '*(i-1), end='')

    #별 2(n-i)+1개
        print('*'*(2*(n-i)+1), end='')
 

    

    else :

        # 블링크 n - x - 1 개
        print(' '*(n-x-1), end='')
        # 별 2x + 1개
        print('*'*(2*x+1), end='')


    print()