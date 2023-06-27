# 문제
# Stan has a deck of 
# $N$ Concentration Cards. He wants to lay the cards edge-to-edge to form a filled rectangle with minimal perimeter. Each card is a rectangle with dimensions 
# $W$ mm by 
# $H$ mm.



# Figure 1: Concentration Cards

# 입력
# The first line of input contains 
# $C$, the number of test cases. For each case there is an additional line containing 
# $N$, 
# $W$, 
# $H$, each a positive integer not exceeding 
# $1000$.

# 출력
# Your program should produce one line of output per case, giving the minimal perimeter.


# 문제 해석 : C 를 받아 입력받을 케이스의 횟수를 정하고, N, H, W 를 각각 입력받아 높이 H, 너비 W인 카드 N장을 가지고 만들수 있는 최소 너비를 찾자.



c=int(input()) # 몇번의 케이스를 실행할 지 입력받기

i = 0

for i in range(c) : # c 번 실행

    n, w, h = input().split() # n : 카드의 장수, w : 카드의 너비, h : 카드의 높이 입력받기 // split()으로 공백마다 값받아오기

    print(n,w,h)

    # 경우 1 - 일직선으로 세워두기
    # 너비와 높이 중 더 작은 수를 N번 세운다!
    # if w > h -> w * 2  + h * 2 * n
    # if w < h -> h * 2  + w * 2 * n

    # 경우 2 - 쌓아서 계산하기
    # 생각한 방법 = 최소공배수를 구해서 h ,w로 나누기 즉, 최소공배수를 만들기위한 값이 각각 나온다.
    # 위의 값을 필요개수라 하고,
    # n / h필요개수의 나머지가 w필요개수로 나누어 떨어진다면 쌓기가 가능하다는 뜻?!
    # ∴ 그때의 둘레는 필요개수를 이용하여 구할 수 있다.
    # n = h필요개수 * p + w필요개수 * q가 되고, 이를 이용하면
    # 둘레  = 최소공배수 * 2 + (w * p + h * q) * 2 // 이때, p 는 n/h필요개수의 몫, q 는 n/w필요개수의 몫이다.

    # 최소공배수 구하는법
    # w,h에 대하여 i를 w,h중 큰수부터 w*h까지 1씩 증가시켜 가며
    # i % w, i % h가 모두 0인 경우 그 수가 최소 공배수