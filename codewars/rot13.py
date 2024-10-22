def rot13(message):
    cipher_table = {}
    for ch in range(0, 26):
        cipher_table[chr(ch + ord('A'))] = chr(((ch + 13) % 26) + ord('A'))
        cipher_table[chr(ch + ord('a'))] = chr(((ch + 13) % 26) + ord('a'))

    return "".join([cipher_table[c] if c in cipher_table else c for c in message])

print(rot13('test'))