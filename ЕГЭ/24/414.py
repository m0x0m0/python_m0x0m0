s = open('414.txt').readline()
k = 0
m = [1] * len(s)
for i in range(5, len(s)):
    if s[i-5:i-2] == 'RUS' and s[i-2:i+1] != 'TEM':
        k += 1
print(k)