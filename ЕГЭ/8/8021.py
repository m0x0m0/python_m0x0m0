word = 'PRODUCT'
print(sum((ord(ch) - ord('A') + 1) * 26**p for ch, p in zip(word[::-1], range(len(word)))))