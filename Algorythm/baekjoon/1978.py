n = int(input())

num_list = []

sosu = []

num_list = list(map(int, input().split()))

for l in num_list:

    yaksu = []

    for i  in range(1, l+1):
        if l % i == 0 :
            yaksu.append(i)
    
    if len(yaksu) == 2:
        sosu.append(l)


print(len(sosu))