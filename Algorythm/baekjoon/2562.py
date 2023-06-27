nums = []

for i in range(9):
    num = int(input())

    nums.append(num)

max = 0
min = nums[0]

for n in nums :
    if max < n :
        max = n
        idx = nums.index(n)+1
    

print(max)
print(idx)