s = open('3020.txt').readline()
m = [0] * len(s)
for i in range(1, len(s)):
    if s[i-1:i+1] == 'ZX' or s[i-1:i+1] == 'ZY':
        if i == 1:
            m[i] = 1
        else:
            m[i] = m[i-2] + 1
print(max(m))