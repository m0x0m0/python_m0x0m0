from itertools import product

k = 0
for w in product('0123456789abcd', repeat=5):
    num = ''.join(w)
    if num[0] != '0':
        if num.count('9') == 1 and len([1 for n in num if n in 'bcd']) <= 3:
            k += 1
print(k)
#133612