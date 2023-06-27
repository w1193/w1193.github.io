names = []          # 과목명
scores = []         # 학점
grades = []         # 점수

for i in range(20):
    name, score, grade = input().split()

    score = float(score)

    names.append(name)
    scores.append(score)
    grades.append(grade)


tot_score = 0
tot_grade = 0

for idx, g in enumerate(grades) :
    if 'P' == g :
        scores[idx] = 0


for idx, g in enumerate(grades) :

    tmp = 0.0

    if 'A' in g :
        tmp = 4.0
    elif 'B' in g :
        tmp = 3.0
    elif 'C' in g :
        tmp = 2.0
    elif 'D' in g :
        tmp = 1.0
    elif 'F' in g :
        tmp = 0.0
    else :
        scores[grades.index(g)] = 0.0


    if '+' in g :
        tmp += 0.5
    if '-' in g :
        tmp -= 0.5

    grades[idx] = float(tmp)


for s, g in zip(scores, grades) :
    tot_score += s
    tot_grade += s*g


print(tot_grade/tot_score)

# tot_score  = 0         # 총 학점
# tot_grade = 0
# p = []


#     tot_grade += tmp * float(score[grades.index(g)])


# for s in scores :
#     tot_score += s

# final_grade = tot_grade / tot_score

# print(final_grade)



