
# Equilateral
# Scalene
# Invalid
# Isosceles


while 1 :
    angles=list(map(int, input().split()))

    if angles[0] == angles[1] == angles[2] == 0:
        break
    
    if sum(angles) - max(angles) > max(angles):

        if len(set(angles)) == 1:
            print("Equilateral")
        elif len(set(angles)) == 2:
            print("Isosceles")
        else:
            print("Scalene")

    else:
        print("Invalid")