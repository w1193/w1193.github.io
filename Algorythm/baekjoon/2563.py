paper = []


for i  in range(1, 101):

    row = []
    for j in range(1, 101):
        row.append(0)
    
    paper.append(row)

# paper가 0으로 가득찬 100 * 100의 매트릭스

# 색종이 만큼 칠하자 ( 1로 칠해서 수를 세주면 편힐듯 )

n = int(input())

for i in range(n):
    x, y = map(int, input().split())

    for o in range(x, x + 10):
        for p in range(y, y + 10):
            paper[p][o] = 1

sum = 0
for p in paper:
    sum += p.count(1)

print(sum)