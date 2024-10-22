n = int(input())
x = float(input())
num = 1
def factorial(number):
   if number == 1:
      return number
   else:
      return number * factorial(number - 1)
import math
print(math.cos(x))

for i in range(1, n+1, 2):
   num -= pow(x, 2*i)/(factorial(2*i))
for i in range(2, n+1, 2):
   num += pow(x, 2*i)/(factorial(2*i))
print(num)