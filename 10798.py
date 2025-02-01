a  = [' '] * 5
for i in range(5):
    a[i] = str(input())

size = []
for i in range(5):
    size.append(len(a[i]))
    
i = 0
for j in range(len(a[i])):
    for i in range(5):
        if j > i:
            print(a[i][j], end = '')
        else:
            print('', end = '')