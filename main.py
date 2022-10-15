try:
    x = int(input('height size-> '))
    y = int(input('width size-> '))

    for i in range(x):
        for j in range(y):
            if i >= j:
                print('*', end=' ')
            else:
                print('*', end=' ')
        print()