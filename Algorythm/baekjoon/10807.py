n = int(input())

nums = input().split()

v = input()

cnt = 0

for i in nums :
    if i == v :
        cnt += 1

print(cnt)