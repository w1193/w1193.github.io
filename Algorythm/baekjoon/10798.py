matrix = []


for i in range(5):
    w = input()
    matrix.append(w)

ans =''

for i in range(15):
    for j in range(5):
        if i < len(matrix[j]):
            ans += matrix[j][i]

print(ans)