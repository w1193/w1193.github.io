import sys

n = int(sys.stdin.readline())

dot = []
dots = []

for i in range(n):
    dot = list(map(int, sys.stdin.readline().split()))
    dot = dot[::-1]
    dots.append(dot)

dots.sort()

for d in dots:
    print(d[1], d[0])

