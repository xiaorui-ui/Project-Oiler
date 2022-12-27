def f(x,i):
    if x%i==0 and x>i:
        print(i)
        return f(x/i,i)
    else:
        return x

def prime(n):
    x=n
    for i in range(2,max(3, int(n**0.5))):
        if x%i==0 and x>i:
            x=f(x,i)
    return x

print(prime(600851475143))
print(f(27,3))
print(prime(906609))