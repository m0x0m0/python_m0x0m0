from re import *

s = open('24-298').readline()

num = r'(?:[789][0789]*)'

pattern = rf'{num}(?:[-*]{num})*'
res = sorted(findall(pattern, s), reverse=1, key=len)
for x in res:
    print(len(x), x)
    input()

#177