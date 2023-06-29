xs = []
ys = []

for i in range(3):
    x, y =map(int,input().split())

    if x not in xs :
        xs.append(x)
    else:
        xs.remove(x)

    if y not in ys:
        ys.append(y)
    else:
        ys.remove(y)

print(xs[0], ys[0])
