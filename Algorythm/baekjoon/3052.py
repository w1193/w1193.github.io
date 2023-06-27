nums = []

for i in range(10):
    n = int(input())
    nums.append(n)

nums_42 = []

for n in nums:
    num = n%42
    nums_42.append(num)


nums_42 = set(nums_42)

nums_42 = list(nums_42)

print(len(nums_42))
