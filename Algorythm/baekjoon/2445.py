n = int(input())

for i in range(1,2*n):
    x = i - n
# i <= n
    if i < n :

    #별 i개
        print('*'*i, end='')

    #블링크 2(n-i)개
        print(' '*(2*(n-i)), end='')

    #별 i개
        print('*'*i)



    else :
        # 별 2n - i 개
        print('*'*(2*n-i), end='')

        # 블링크 2x개
        print(' '*(2*x), end='')

        # 별 2n - i개
        print('*'*(2*n-i))