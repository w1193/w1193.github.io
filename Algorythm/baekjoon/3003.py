# 1 1 2 2 2 8

correct = [1,1,2,2,2,8]

chess = input().split()

how_much=[]

for i in range(6) :
    chess[i] = int(chess[i])
    how_much.append(0)


for i in range(6) :
    how_much[i] = correct[i] - chess[i]

for h in how_much:
    print(h, end = ' ')