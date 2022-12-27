def f(x):
    if x%2==0:
        return x/2
    else:
        return (3*x+1)

def length(n):
    if n==1:
        return 1
    else:
        return 1+length(f(n))

def maxlength(n):
    maxl=1
    max=1
    for i in range (1, n+1):
        if length(i)>maxl:
            maxl=length(i)
            max=i
    return max


print(maxlength(1000000))


