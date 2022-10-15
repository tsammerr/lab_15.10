try:
    x = int(input('side size -> '))
    for i in range(x):
        for j in range(x):
            if i == 0 or i == x - 1:
                print(f'* ', end=' ')
            else:
                if j == 0 or j == x - 1:
                 print(f'* ', end=' ')
                else:
                 print(f'  ', end=' ')

        print()
except Exception as ex:
    print(ex)