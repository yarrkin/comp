def mymatrix(x):
    print(' ', end='')
    for i in range(1, x + 1):
        print(str(i).rjust(3), end='')
    print()
    for i in range(1, x + 1):
        print(i, end='')
        for j in range(1, x + 1):
            print(str(i * j).rjust(3), end='')
        print()

mymatrix(5)