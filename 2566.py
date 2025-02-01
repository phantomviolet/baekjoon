a = [[0] * 9 for i in range(9)]
a = [list(map(int, input().split())) for i in range(9)]
tmp = a[0][0]
x, y = 0, 0
for i in range(9):
    for j in range(9):
        if tmp < a[i][j]:
            tmp = a[i][j]
            x, y = i, j
            
print(tmp) 
print(x+1, y+1)