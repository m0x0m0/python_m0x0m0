from re import *

s = open('k7a-1.txt').readline()
pattern = r'[ABC]+'

# print(findall(pattern, s[:100])) проверка что регулярка работает
print(max(len(c) for c in findall(pattern, s)))