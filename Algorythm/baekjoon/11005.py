n, b = map(int, input().split())       # n = 주어진 수 / b = b진법

nums = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'   # 0-35 순서

ans = ''

while n != 0:
    ans += str(nums[n%b])
    n //= b

ans = ans[::-1]

print(ans)