# this problem wants you to find both 4-digit increasing arithmetic sequences s.t. all 3 terms are prime
# permutation of each others' digits. 

# variables: first number n, and increment 9*k(mod 9 is invariant)
# keep a set/dict of primes and non-primes each for easy referral

primes = set()
composites = set()

#need n + 18*k < 10_000
#1000, 1001, 1002 are clearly composites so start from 2003

def is_prime(n):
    if n in primes:
        return True
    elif n in composites:
        return False
    else:
        for m in range(2, int(n**0.5) + 1):
            if (not n%m):
                composites.add(n)
                return False
        primes.add(n)
        return True

def digits(n):
    lis = []
    for i in range(4):
        lis += [n%10]
        n = n//10
    lis.sort()
    return lis
        
for n in range(1003, 10_000):
    if not is_prime(n):
        continue
    for k in range(1, (9999 - n)//18 + 1):
        if is_prime(n + 9*k) and is_prime(n + 18*k):
            if digits(n) == digits(n + 9*k) == digits(n + 18*k):
                print(n, k)





