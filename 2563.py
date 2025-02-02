a = [[0] * 100 for i in range(100)]
size = 10

t = int(input())
for i in range(t):
    row, col = map(int, input().split())
    for j in range(size):
        for k in range(size):
            a[j + row][k + col] += 1

count = 0
for i in range(100):
    for j in range(100):
        if a[i][j] > 0:
            count += 1
            
print(count)