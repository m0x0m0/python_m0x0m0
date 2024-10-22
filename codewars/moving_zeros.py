def move_zeros(lst):
    zero, new = [], []
    for i in range(len(lst)):
        if lst[i] != 0:
            new.append(lst[i])
        else:
            zero.append(lst[i])
    return new + zero


def move_zeros_1(a):
    a.sort(key=lambda v: v == 0)
    return a