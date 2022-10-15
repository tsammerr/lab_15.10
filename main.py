try:
    x = int(input('height size -> '))
    y = int(input('width size -> '))
    for i in range(x):
        for j in range(y):
            if i == 0 or i == x - 1:
                print(f'* ', end=' ')
            else:
                if j == 0 or j == y - 1:
                 print(f'* ', end=' ')
                else:
                 print(f'  ', end=' ')

        print()
except Exception as ex:
    print(ex)