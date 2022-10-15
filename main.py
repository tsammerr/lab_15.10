try:
    x = int(input('side size -> '))
    for i in range(x):
        if j == 0 or j == x - 1:
            print('  ', end=' ')
        else:
            print('  ', end=' ')
        for in range(x):
            if i == 0 or i == x - 1:
                print('* ', end=' ')
            else:
                print('  ', end=' ')
        print()
except Exception as ex:
    print(ex)