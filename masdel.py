def masdel(args):
    mymax = max(args) // 2
    mylist = []
    for i in range(2, mymax):
        for x in args:
            if x % i != 0:
                break
        else:
            mylist.append(i)
    return print(mylist)


masdel([42, 12, 18])