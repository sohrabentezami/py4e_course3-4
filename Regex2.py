import re

fname = input('Enter the file name: ')
fhand = open(fname)
numlist=list()

for line in fhand:
    line = line.rstrip()
    x = re.findall('[0-9]+',line)
    if len(x) < 1 : continue
    for word in x :
        numlist.append(int(word))

print(sum(numlist))
