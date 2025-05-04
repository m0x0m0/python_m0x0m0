s = open('1874.txt').readline()

m = [1] * len(s)
for i in range(len(s)):
    if s[i-1] != 'Q' and s[i] != 'W':
        m[i] = m[i-1] + 1
print(max(m))


for i in range(2, len(s)):
    if s[i-2:i+1] != 'PPP':
        m[i] = m[i-1] + 1
print(max(m))