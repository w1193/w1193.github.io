n = int(input())

list = input().split()

for i in range(n) :
    list[i] = int(list[i])

max = 0

for l in list:
    if max < l :
        max = l

avg = 0

for l in list:
    avg += (l*100/max)/n
    

print(avg)