try:
    x = int(input('side size -> '))
    for i in range(x):
        for j in range(x):
            print('*', end=' ')
        print()
except Exception as ex:
    print(ex)