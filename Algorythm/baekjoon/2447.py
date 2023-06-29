# 재귀! 결과적으로는
#  123 
#  456   다음 모양에서 5번을 뺀 나머지를 1번으로 채워진 모양을 계속해서 저장해 나가는 방식
#  789

# n = 3 일때의 모습을 5 빼고 집어 넣으면 n = 9



n = int(input())

def star(l):
    if l == 3:
        return ['***','* *','***']

    arr = star(l//3)
    stars = []

    for i in arr:
        stars.append(i*3)

    for i in arr:
        stars.append(i+' '*(l//3)+i)

    for i in arr:
        stars.append(i*3)

    return stars

print('\n'.join(star(n)))


# 공부 필요