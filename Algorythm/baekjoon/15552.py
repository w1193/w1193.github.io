import sys

T = int(sys.stdin.readline().rstrip())

for i in range(T) :
    a,b = input().split()
    a = int(a)
    b = int(b)

    print(a+b)