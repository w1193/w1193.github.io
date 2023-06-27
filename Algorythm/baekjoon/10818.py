n = int(input())

nums = input().split()

max = int(nums[0])
min = int(nums[0])

for n in nums :

    if max < int(n) :
        max = int(n)

    if min > int(n) :
        min = int(n)

print(min, max)