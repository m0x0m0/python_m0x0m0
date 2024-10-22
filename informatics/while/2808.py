n = int(input())
s = str(n) + ' '
for i in range(1, n):
    s = s + str(i) + ' '
print(s[:-1])