b, n = input().split()       # b = 주어진 수 / n = n진법

n = int(n)

num = 0

b_list = []

for b in b :
    b_list.append(b)


nums = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'   # 0-35 순서

list = []

for l in b_list :
    list.append(nums.find(l))                   # idx를 찾아서 몇인지 찾기

for idx, l in enumerate(list[::-1]):
    num += l * (n ** idx)

print(num)