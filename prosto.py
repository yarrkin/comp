def prosto(a, b):
    mylist = []
    for x in range(a, b + 1):
        for i in range(2, x // 2):
            if x % i == 0:
                break
        else:
            mylist.append(x)
    return print(mylist)

prosto(11, 20)