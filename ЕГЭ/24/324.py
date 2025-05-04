from re import *
s = open('324.txt').readline()
print(s[:50])
pattern = r'[A-Z]+'

res = len(max(sorted(findall(pattern, s), reverse = 1, key = len), key = len))
print(res)