x = int(input('i->'))
y = int(input('j->'))

for i in range(x):
    for j in range(y):
        if i >= j:
           print('*', end=' ')
        else:
            print('*', end=' ')
    print()