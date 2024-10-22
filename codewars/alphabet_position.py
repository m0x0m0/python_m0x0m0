numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u','v', 'w', 'x', 'y', 'z']
slvr = dict(zip(alphabet, numbers))

def alphabet_position(text):
    text = text.lower()
    txt = (s for s in text if str(s) not in " 1234567890,./!@#$%^';:*?)(")
    lst = [slvr[el] for el in txt]
    stro = ''
    for el in lst:
        stro = stro + str(el) + ' '
    return stro[:-1]
alphabet_position(input())