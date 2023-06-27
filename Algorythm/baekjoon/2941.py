string = input()

cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for c in cro :
    string = string.replace(c, ' ')  
print(len(string))
