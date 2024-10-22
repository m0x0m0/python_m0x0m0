marks = input().split()
marks = [int(el) for el in marks]
k = 1
suma = marks[0]

for i in range(1, 10):
    k += 1
    suma += marks[i]
    if marks[i - 1] == 2 and marks[i] != 2:
        suma -= marks[i - 1]
        k -= 1

print(int(suma / k))