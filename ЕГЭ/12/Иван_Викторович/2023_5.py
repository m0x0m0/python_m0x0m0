s = '>' + 20*'1' + 15*'2' + 40*'3'
while '>1' in s or '>2' in s or '>3' in s:
    if '>1' in s:
        s = s.replace('>1', '22>', 1)
    if '>2' in s:
        s = s.replace('>2', '2>1', 1)
    if '>3' in s:
        s = s.replace('>3', '1>2', 1)
print(sum([int(i) for i in s if i != '>']))