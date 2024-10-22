n = int(input())
maxi = 0
lst = []
while n != 0:
    if n not in lst:
        lst.append(n)
    if n > maxi:
        maxi = n
    n = int(input())
lst.remove(maxi)
print(max(lst))