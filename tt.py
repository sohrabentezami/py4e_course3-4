import re

hand = open("regex_sum_42.txt")
x=list()
for line in hand:
     y = re.findall('[0-9]+',line)
     print(y)
     if len(y) < 1 : continue
     x = x+y
print(x)

sum=0
for z in x:
    sum = sum + int(z)

print(sum)
