m, d = map(int, input().split())            # m = 월 / d = 일

days = 0                                    # 1월 1일 부터 일수

week = ["MON","TUE","WED","THU","FRI","SAT","SUN"]

month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]



for i in range(m-1):                        # 1월부터 m 까지 날짜 더하기
    days = days + month[i]                  
yoil = (days + d)% 7 - 1                       # 요일이니 7로 나눠주기 / mon = 0이니 -1
 
print(week[yoil])