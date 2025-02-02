a  = [' '] * 5
for i in range(5):
    a[i] = str(input())
    
max_len = max(len(row) for row in a)
for j in range(max_len):
    for i in range(5):
        if j >= len(a[i]):
            continue
        else:
            print(a[i][j], end='')
            