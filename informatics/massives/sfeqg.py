from math import isprime
number = 17
result = isprime(number)
if result:
    print(f"{number} - простое число")
else:
    print(f"{number} - составное число")