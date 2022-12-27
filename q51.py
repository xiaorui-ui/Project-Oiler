# again, create a set of primes and composites. Then whack all the permutations? 
# Idk.
# cannot whack last digit clearly for mod 2 reasons, and need to whack a multiple
# of 3 digits for mod 3 reasons.
# Also since the selected prime is the smallest, the same block of digits need to 
# be <= 2.
# answer is probably >> 56003 but we'll see.

from itertools import combinations

# primes = set()
# composites = set()
primes = []
curr = 56003

def is_prime(n):
    if n < 2:
        return False
    elif n in primes:
        return True
    # elif n in composites:
    #     return False
    else:
        for m in primes:
            if m <= int(n**0.5):
                if (not n%m):
                    # composites.add(n)
                    return False
            else:
                break
        primes.append(n)
        return True

for i in range(curr):
    is_prime(i)

print(primes)

comb = combinations([0, 1, 2, 3], 3)
while True:
    string = str(curr)
    boo = False
    if len(string) > len(str(curr - 1)):
        comb = combinations(list(range(len(string) - 1)), 3)

    if not is_prime(curr):
        curr += 1
        continue

    for x in list(comb):
        if int(string[x[0]]) < 3:
            if string[x[0]] == string[x[1]] == string[x[2]]:
                count = 0
                for i in range(10):
                    new = string[:x[0]] + str(i) + string[x[0]+1:x[1]] + str(i)\
                        + string[x[1]+1:x[2]] + str(i) + string[x[2]+1:]
                    count += int(is_prime(int(new)))
                if count >= 8:
                    boo = True
                    print(x)
                    break
    
    if boo:
        print(curr)
        #print(primes)
        break
    curr += 1

# this one is too slow cos you're checking every number. Actually you can check only those 
# with >= 3 repetitions.





    



