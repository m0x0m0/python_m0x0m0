n = int(input()) #число в 10-ой
cc = int(input()) #нужное нам основание сс
result = ''

while n > 0:
    result = str(n % cc) + result
    n //= cc
print(result)