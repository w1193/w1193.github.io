n = int(input())

def recursion(s, l, r, cnt):

    if l >= r: 
        return print(1, cnt)
    elif s[l] != s[r]: 
        return print(0, cnt)
    else: 
        return recursion(s, l+1, r-1, cnt+1)
    

def isPalindrome(s, cnt):
    return recursion(s, 0, len(s)-1,cnt)


for i in range(n):
    str = input()
    isPalindrome(str, 1)
    
    
    # print( isPalindrome('ABBA',0))
    # print( isPalindrome('ABC',0))
