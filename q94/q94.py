peri_sum = 0;

# area = sqrt((s-a)(s-b)(s-c)s)
# we must have a=b=odd, c=even
# range(start, end, rage), start from 3 so that's it's non-degenerate

for i in range(3, 333_333_334, 2):
    j = 3*i + 1
    area1 = (i - 1)*(3*i + 1)
    k = 3*i - 1
    area2 = (i + 1)*(3*i - 1)
    if area1**0.5 == int(area1**0.5):
        peri_sum += j
    if area2**0.5 == int(area2**0.5):
        peri_sum += k

print(peri_sum)

#11138120726
#through simple shell tests, we find that the precision of == isn't sufficient
        
    
    
    
    
