import sys

n = int(sys.stdin.readline())

strings = []

for i in range(n):
    strings.append(sys.stdin.readline())

strings = list(set(strings))

strings.sort()
strings.sort(key=len)

for s in strings:
    print(s, end='')