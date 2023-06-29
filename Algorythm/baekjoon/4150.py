a= 1
b =1

n = int(input())

for i in range(n-2):
    tmp = 0

    tmp = b
    b = a + b
    a = tmp


print(b)