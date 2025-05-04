f = open('9.txt')

k = 0
for s in f:
    a = list(map(int, s.split()))
    povt = [el for el in a if a.count(el) == 2]
    print(a, povt)
    if (max(a) < (sum(a) - max(a))) and len(set(a)) == 3:
        k += 1
print(k)