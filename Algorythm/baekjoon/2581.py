m = int(input())
n = int(input())

sosu = []

sum = 0

for l in range(m, n+1):
     
    yaksu = []

    for i  in range(1, l+1):
        if l % i == 0 :
            yaksu.append(i)
    
    if len(yaksu) == 2:
        sosu.append(int(l))

if len(sosu) > 0:
    for s in sosu:
        sum += s
    
    print(sum)
    print(sosu[0])

else:
    print('-1')