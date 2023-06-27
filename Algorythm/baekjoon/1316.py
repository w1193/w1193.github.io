n = int(input())
cnt = n

for i in range(n):

    string = input()

    for j in range(0, len(string)-1):
        if string[j] == string[j+1]:
            continue

        elif string[j] in string[j+1:]:
            cnt -= 1
            break

print(cnt)