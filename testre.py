import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    y = re.findall('\S+@\S+', line)
    print(y)
