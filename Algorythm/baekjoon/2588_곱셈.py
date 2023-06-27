a = input("")

b = input("")

int_a = int(a)
int_b = int(b)

b_1 = b[2]
b_10 = b[1]
b_100 = b[0]

# (3) = b의 3번째 * a

num3 = int_a * int(b_1)

print(num3)


# (4) = b의 2번째 * a
num4 = int_a * int(b_10)

print(num4)

# (5) = b의 1번째 * a
num5 = int_a * int(b_100)

print(num5)

# (6) = a * b

num6 = int_a * int_b

print(num6)