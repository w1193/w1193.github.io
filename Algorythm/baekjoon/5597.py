nums = []

for i in range(1,31):
    nums.append(i)

max = 0
min = 0

for i in range(28) :
    num = int(input())

    if num in nums :
        nums.pop(nums.index(num))

print(nums[0])
print(nums[1])