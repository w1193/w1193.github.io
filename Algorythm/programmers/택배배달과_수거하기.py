# n : 집의 개수, i : 집과 창고 사이 거리, cap : 택배트럭의 용량
# deliveries : 배달할 재활용 상자의 양, pickups: 수거할 상자의 양
# ex)    [1, 0, 3, 1, 2]       /       [0, 3, 0, 4, 0]


# answer : 최소이동거리

# 문제 풀이 
# - 뒤에서 부터 cap 이하까지 배달할 수 있는 택배 계산.
# - 뒤에서 부터 cap 까지 배달하며, 돌아올때, 들수있는 수거용 상자 계산
# - 반복

# 뒤에서 부터 계산? 스택을 사용하자




def solution(cap, n, deliveries, pickups):
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    answer = 0

    have_to_deli = 0
    have_to_pick = 0

    for i in range(n):
        have_to_deli += deliveries[i]
        have_to_pick += pickups[i]

        while have_to_deli > 0 or have_to_pick > 0:
            have_to_deli -= cap
            have_to_pick -= cap
            answer += (n - i) * 2

    return answer



print(solution(2, 7, [1,0,2,0,1,0,2], [0,2,0,1,0,2,0]))