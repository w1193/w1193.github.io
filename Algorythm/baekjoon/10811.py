n , m = map(int, input().split())

bask = []

for i in range(n) :
    bask.append(i+1)

for i in range(m):
    i, j = map(int, input().split())
    
    tmp = bask[i-1:j]
    tmp.reverse()
    bask[i-1:j] = tmp

for b in bask :
    print(b, end =' ')