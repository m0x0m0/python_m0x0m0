n = int(input())
list1 = list(map(int, (input()).split()))
list1.reverse()
print(*list1, sep=' ')