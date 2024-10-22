lst = [0] * int(input())
lst[len(lst)//2 - 1] == 1 and print(lst) if len(lst) % 2 == 0 else lst[len(lst)//2] = 1 and print(lst)