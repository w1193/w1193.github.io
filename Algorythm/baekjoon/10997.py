n = int(input())

# 높이 = 4 n - 1    /   너비 = 4 n -3

hei = 4 * n - 1                # 높이
wid = 4 * n - 3          # 너비

stars = [[' ' for w in range(wid)] for h in range(hei)]    # 별이 들어가야 할 리스트 초기화


def draw(x , y , n):

    width = 4 * n - 3
    height = 4 * n - 1

    if n == 1:
        stars[y][x] = '*'
        stars[y+1][x] = '*'
        stars[y+2][x] = '*'     # 1 일때 위로 3개 쌓고 종료
        return
    
    else :
        for i in range(width - 1):          # 윗줄
            stars[y][x] = '*'
            x -= 1                          # x를 1칸씩 없애가면서 전부 별          시작점 오른쪽 맨위

        for i in range(height - 1):         # 왼쪽 줄
            stars[y][x] = '*'
            y += 1                          # y를 내려가면서 위쪽으로 전부 별       시작점 왼쪽 맨 위

        for i in range(width - 1):          # 아랫줄
            stars[y][x] = '*'
            x += 1                          # x를 늘려가면서 오른쪽으로 전부 별     시작점 왼쪽 맨 아래



        for i in range(height - 3) :        # 오른쪽 줄 - 차이 존재 / 마지막에 한칸 꺾어야 함  / 한칸 덜 가기 위해 -2 추가 (끝에서 두번째가 끝이므로)
            stars[y][x] = '*'
            y -= 1                          # x를 늘려가면서 오른쪽으로 전부 별 (마지막 한칸 남기기)


        stars[y][x] = '*'                   # 마지막 별 그려주고
        stars[y][x - 1] = '*'               # 마지막에 왼쪽으로 한칸 꺾으면서 끝

        draw(x - 2, y, n-1)                 # 재귀


if n == 1 :
    print('*')               # 1 일때는 하나만 출력

else :
    draw(wid - 1, 0, n)                 

    for s in stars:
        print(''.join(s).rstrip())