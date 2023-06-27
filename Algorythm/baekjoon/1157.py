string = input().upper()

set_string = []

for s in string :
    set_string.append(s)

set_string = set(set_string)
set_string = list(set_string)


for s in set_string :

    cnt = 0

    for ss in string :
        if ss == s :
            cnt += 1

    if cnt > max_cnt:
        max_cnt = cnt
        max_str = s

    elif cnt == max_cnt :
        max_cnt = cnt
        max_str = '?'

    # print(max_cnt, max_str)

print(max_str)