T = int(input())   # 테스트 케이스 개수

for i in range(T) :
    a, b = input().split()
    a = int(a)
    b = int(b)

    print(f"Case #{i+1}: {a+b}")