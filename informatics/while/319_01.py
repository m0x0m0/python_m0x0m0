a = float(input())
n = int(input())
sum = 1
an = 1

for i in range(1, n+1):
    an *= a
    sum += an

print("{:.8f}".format(sum))