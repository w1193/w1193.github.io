n, m = map(int, input().split())              # n = 리스트 크기 / m = 변경 횟수

balls = []

for y in range(n) :
    balls.append(0)

for y in range(0, m) :
    i, j , k = input().split()
    i = int(i)
    j = int(j)
    k = int(k)

    while i != j+1 :
        
        balls[i-1]= k
        i += 1

for b in balls :
    print(b , end = " ")