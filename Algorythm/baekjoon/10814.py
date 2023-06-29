import sys

n = int(sys.stdin.readline())

lists = []

for i in range(n):
    age, name = map(str, sys.stdin.readline().split())
    age = int(age)
    lists.append((age, name))

lists.sort(key = lambda x : x[0])	

for l in lists:
    print(l[0], l[1])