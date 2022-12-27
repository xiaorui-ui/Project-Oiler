def recurse(n,s):
    """
    print string 's' once, then print it n more times
    """
    if n==0:
        print(s)
    else:
        print(s, recurse (n-1,s))

recurse(3,5)
#recurse(-1,0)

import time
x=int(time.time())
print(x//(3600*24), 'days', x%(3600*24)//(3600), 'hours', (x%(3600*24))%3600//60, 'mins', (x%(3600*24))%3600%60, 'seconds')

#actually we can also do years and days just that it's a bit tougher
#let's try that

y=-0.75+((x//(3600*24)//365.25-1)%4)*0.25
print(x//(3600*24)//365.25, 'years',x//(3600*24)%365.25+y,'days')


x=input('What is your length?'); y=input('What is the length of Bobby?'); z=input('What is the length of the guy she told you not to worry about?')
a=int(x); b=int(y); c=int(z)
def if_love_triangle(a,b,c):
    if (a+b)>c and (a+c)>b and (b+c)>a:
        print('yes')
    elif (a+b)<c or (a+c)<b or (b+c)<a:
        print('no')
    else:
        print('denegenerate THIS IS SO SAD')

print(if_love_triangle(a,b,c))






