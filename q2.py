def F(n):
    if n==1:
        return 1
    if n==2:
        return 1
    else:
        return F(n-2)+F(n-1)

print(F(35))

def sumto(n):
    total=0
    for x in range(1, n):
        if x%3==0 and F(x)<=4*(10**6):
            total=total+F(x)
    return total
print(sumto(35))

