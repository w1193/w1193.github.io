n = int(input())

# 높이 = 너비 = 4n -3 = 길이

len = 4*n - 3



stars = [[' ' for w in range(len)] for h in range(len)]   # 그릴 별 행렬 초기화


# 함수 시작

# 첫줄과 끝줄은 전체 별, 나머지는 양끝만 별

def draw(w, h, n):          # w = 시작 너비 / h = 시작 높이 / n = 차수
    
    length = 4*n - 3        # 함수 시작마다 길이 초기화
    
    if n == 1 :                      # n = 1이 되면
        stars[h][w] = '*'            # 마지막 별 찍어주고
        return                       # 함수 끝내기

    else:
        

        for y in range(length):
            stars[h][w + y] = '*'               # 맨 위줄
            stars[h + y][w] = '*'               # 왼쪽 줄
            stars[h + length - 1][w + y] = '*'  # 오른쪽 줄
            stars[h + y][w + length - 1] = '*'  # 맨 아래줄

                

        draw(w + 2, h + 2, n - 1)


draw(0 , 0, n)

for i in stars:
    print(''.join(i).rstrip())
