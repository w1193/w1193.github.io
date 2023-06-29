a, b, v = map(int, input().split())

# now = 0
# cnt = 0

# while now < v:
#     now += a
#     cnt+=1
#     if now < v:
#         now -= b

# 시간 초과

cnt = (v - b) / (a - b)

if cnt == int(cnt):
    cnt = int(cnt)

else :
    cnt = int(cnt) + 1

print(cnt)