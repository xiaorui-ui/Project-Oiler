#s=input('bruh')
#def isPalindrome(s):
   #return s == s[::-1]

#output=true or false

def f(x):
    for z in range(x, 1, -1):
        if str(z)==str(z)[::-1]:
            if g(z)==1:
                return z


def g(x):
    y = (x + 998) // 999
    a=0
    for z in range(999,y-1,-1):
        if x%z==0:
            a=1
    return a

print(f(999**2))


