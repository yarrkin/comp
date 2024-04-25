def comp(x):
    y = int(str(x)[-1::])
    if y == 1:
        return print(x, 'компьютер')
    elif y in range(2, 5):
        return print(x, 'компьютера')
    else:
        return print(x, 'компьютеров')

comp(int(input()))