import sys

N  = int(sys.stdin.readline())
num_list = [0]*10000001

for _ in range(N):
    num = int(sys.stdin.readline())
    num_list[num] += 1 

for i in range(10001): 
    if num_list[i] != 0:
        for j in range(num_list[i]): 
            print(i)