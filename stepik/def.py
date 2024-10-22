def is_prime(num):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
    return (count == 2)

n = int(input())

for i in range(1, 20):
   if is_prime(n + i):
      print(n + i)
      break