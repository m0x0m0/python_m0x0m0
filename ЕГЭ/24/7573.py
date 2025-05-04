from re import *

s = open('24-299').readline()

num = r'(?:[1-9][0-9]*|0)'
pr = rf'(?:(?:{num}\*)*0(?:\*{num})*)'
pattern = rf'(?:{pr}\+)*{pr}(?:\+{pr})*'

res = sorted(findall(pattern, s), reverse = 1, key = len)
for x in res:
    print(len(x), x)
    input()