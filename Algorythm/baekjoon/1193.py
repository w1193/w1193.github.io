n = int(input())

daegak = 0
end = 0

ans = ''

while n > end:
    daegak += 1
    end += daegak

tot = end - n

if daegak % 2 == 0:                 # 짝수면 오른쪽 시작
    a = daegak - tot
    b = tot + 1

else :
    b = daegak - tot                # 홀수면 왼쪽 시작
    a = tot + 1



ans = str(a) + '/' + str(b)

print(ans)