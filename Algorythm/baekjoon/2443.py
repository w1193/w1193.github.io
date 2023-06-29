n = int(input())

for i in range(n) :
    print('*'*(2*(n-i)-1))
    print(' '*(i+1), end='')
    