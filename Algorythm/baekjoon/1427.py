import sys

num = str(sys.stdin.readline())

num_list = []

for n in num :
    num_list.append(n)

num_list.sort(reverse=True)

ans = ''

for n in num_list:
    ans += n

print(int(ans))