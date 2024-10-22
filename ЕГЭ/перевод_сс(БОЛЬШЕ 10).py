n = int(input()) #число в 10-ой
cc = int(input()) #нужное нам основание сс
result = ''
lst = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

while n > 0:
    result = lst[n % cc] + result
    n //= cc
print(result)