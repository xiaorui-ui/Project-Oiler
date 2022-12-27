lis = []

for i in range(100):
    if (i**0.5) == int(i**0.5):
        continue
    curr = 1
    while True:
        if ((1 + i*curr**2)**0.5) == int((1 + i*curr**2)**0.5):
            lis += [[i, curr]]
            break
        curr += 1

print(lis)
