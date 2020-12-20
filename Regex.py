import re

fname = input('Enter the file name: ')
fhand = open(fname)
numlist=list()

for line in fhand:
    line = line.rstrip()
    x = re.findall('[0-9]+',line)
    if len(x) < 1: continue
    i = 0
    while i<len(x) :
        numlist.append(int(x[i]))
        i = i+1
    i = 0

print(sum(numlist))
