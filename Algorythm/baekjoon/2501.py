n , k = map(int,input().split())

list = [0, ]

for i  in range(1, n+1):
    if n % i == 0 :
        list.append(i)

if len(list) > k:
    print(list[k])

else:
    print('0')