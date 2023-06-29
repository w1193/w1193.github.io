row = []


for i in range(9):
    row.append(0)

max = 0
max_idx_row = 0
max_idx_col = 0

tmp = 0

for i in range(9):

    row = list(map(int, input().split()))

    for idx, r in enumerate(row):

        if tmp <= r:
            max = r
            max_idx_row = idx+1
            max_idx_col = i+1
            
            tmp = r


print(max)
print(max_idx_col, max_idx_row)

        