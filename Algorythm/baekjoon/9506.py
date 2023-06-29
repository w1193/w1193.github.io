while 1 :
    
    list = []
    sum = 0
    n = int(input())

    if n == -1:
        break

    ans = ''
    ans += str(n)

    for i  in range(1, n):
        if n % i == 0 :
            list.append(str(i))
            sum += i


    if sum == n :
        ans += ' = '
        ans += ' + '.join(list)

        print(ans)

    else :
        ans += ' is NOT perfect.'

        print(ans)