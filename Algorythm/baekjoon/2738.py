
a, b = [], []

n, m = map(int, input().split())

for r in range(n):
    r = input().split()

    for i in range(len(r)) :
        r[i] = int(r[i])

    a.append(r)

for r in range(n):
    r = input().split()

    for i in range(len(r)) :
        r[i] = int(r[i])

        
    b.append(r)
    
for r in range(n):
    for c in range(m):
        print(a[r][c] + b[r][c], end=' ')
    print()