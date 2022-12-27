# use a dictionary, key is tuple of digits, value is number of appearances
# the moment key hits 5, stop

dic = {}

def q62():
    curr = 1
    while True:
        x = curr**3
        digits = list(str(x))
        digits.sort()
        digits = tuple(digits)
        if digits not in dic:
            dic[digits] = []
        if len(dic[digits]) == 25:
            return (min(dic[digits]))**3
        dic[digits] += [curr]
        curr += 1

print(q62())

# actually this only happens to work for 5; for any N you need to make sure 
# you check all those with the same number of digits and select the smallest.
# every time you hit something w/ N you can add it to a list and when curr**3 
# is too big you sort the list.



