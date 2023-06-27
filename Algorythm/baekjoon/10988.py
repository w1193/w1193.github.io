string = str(input())
check = False
rev = ''

for s in string[::-1] :
    rev += s



if rev == string :
    print("1")

else:
    print("0")

