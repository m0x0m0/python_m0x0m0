def persistence(num):
    if len(str(num)) == 1:
        return 0
    else:
        count = 0
        while len(str(num)) > 1:
            proizv = 1
            num_lst = [int(i) for i in str(num)]
            for el in num_lst:
               proizv *= el
            num = proizv
            count += 1
        return count



