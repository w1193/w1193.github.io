
n = int(input())

# 높이 = 2 ^ n - 1    /   너비 = 2 ^ (n + 1) - 3

hei = 2 ** n - 1                # 높이
wid = 2 ** (n + 1) - 3          # 너비

# for h in range(hei):
#     for w in range(wid):
#         stars[w][h].append(' ')


stars = [[' ' for w in range(wid)] for h in range(hei)]    # 별이 들어가야 할 리스트




# 함수 시작


def draw(w, h, n) :                  # 별그려주기 함수 (재귀) / h = 그리기 시작하는 높이값 / w = 그리기 시작하는 너비값 / n = n번째 삼각형

    if n == 1 :                      # n = 1이 되면
        stars[h][w] = '*'            # 마지막 별 찍어주고
        return                       # 함수 끝내기
    

    height = 2 ** n - 1                   # 재귀때마다 높이 / 너비 초기화
    width = 2 ** (n + 1) - 3

    # 홀수면 정방향 삼각형  /  짝수면 역방향 삼각형

    # 홀수 일때
    
    if n % 2 == 1:
        for i in range(width):
            stars[h][w + i] = '*'                       # 밑변

        for i in range(height):
            stars[h - i][w + i] = '*'                   # 옆면 1
            stars[h - i][w + width - i - 1] = '*'       # 옆면 2

        draw(w + (2 ** (n - 1)), h - (2 ** (n - 1) - 1), n -1)  # 다음 번 그림 그리기 - 그리는 지점은 멀고 낮아지고(w,h) , 차수(n)는 내리기
    
    # 짝수 일때

    else :
        for i in range(width):
            stars[h][w + i] = '*'                       # 밑변

        for i in range(height):
            stars[h + i][w + i] = '*'                   # 옆면 1
            stars[h + i][w + width - i - 1] = '*'       # 옆면 2
    
    
        draw(w + (2 ** (n - 1)), h + (2 ** (n - 1) - 1), n -1)  # 다음 번 그림 그리기 - 그리는 지점은 멀고 높아지고(w,h) , 차수(n)는 내리기



# 별그리기 함수 끝

if n % 2 == 1:
    draw(0, hei - 1, n)         # 홀수일때는 밑에서 시작

else :
    draw(0, 0, n)               # 짝수일때는 위에서 시작


for i in stars:
    print(''.join(i).rstrip())          # 공백있어서 틀림...

