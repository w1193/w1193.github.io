n = int(input())

soinsu = []


     
yaksus = []

for i in range(1, n+1):
    if n % i == 0 :
        yaksus.append(i)


for y in yaksus:
    
    yaksu = []

    for i in range(1, y+1):
        if y % i == 0 :
            yaksu.append(i)
    
    if len(yaksu) == 2:
        soinsu.append(int(y))

times = []

for s in soinsu:

    tmp = n
    cnt = 0
    
    while tmp % s == 0:
        tmp = tmp // s
        cnt += 1
    
    times.append(cnt)

for s, t in zip(soinsu, times):
    print(f'{s}\n'*t, end='')