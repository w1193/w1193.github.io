import sys

n = int(sys.stdin.readline())

dot = []
dots = []

for i in range(n):
    dot = list(map(int, sys.stdin.readline().split()))
    dots.append(dot)

dots.sort()

for d in dots:
    print(d[0], d[1])


# for i in range(n-1):
#     tmp = []

#     if dots[i][0] > dots[i+1][0]:
#         tmp = dots[i][0]
#         dots[i][0] = dots[i+1][0]
#         dots[i+1][0] = tmp

#         tmp = dots[i][1]
#         dots[i][1] = dots[i+1][1]
#         dots[i+1][1] = tmp

#     elif dots[i][0] == dots[i+1][0]:
#         if dots[i][1] > dots[i+1][1]:
#             tmp = dots[i][0]
#             dots[i][0] = dots[i+1][0]
#             dots[i+1][0] = tmp

#             tmp = dots[i][1]
#             dots[i][1] = dots[i+1][1]
#             dots[i+1][1] = tmp


# for d in dots:
#     print(d[0], d[1])