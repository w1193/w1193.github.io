n = int(input())

on = 1              # 시작 = 1

how_many = 1        # 몇번 이동?

while n > on :
    on += 6 * how_many
    how_many += 1

    # 6 + (6 + 6) + (6 + 6 + 6) + ...

print(how_many)