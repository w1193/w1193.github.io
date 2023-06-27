n , m = map(int, input().split())

balls = []

for i in range(n) :
    balls.append(i+1)

for i in range(m) :
    i, j = map(int, input().split())

    tmp = balls[i-1]

    balls[i-1] = balls[j-1]

    balls[j-1] = tmp

for b in balls :
    print(b, end = " ")