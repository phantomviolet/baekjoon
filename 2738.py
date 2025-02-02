N, M = map(int, input().split())
a = [0 for i in range(N)]
b = [0 for i in range(N)]
c = [[0]*M for i in range(N)]

for i in range(N):
    a[i] = list(map(int, input().split()))
    
for j in range(N):
    b[j] = list(map(int, input().split()))
    
for i in range(N):
    for j in range(M):
        c[i][j] = a[i][j] + b[i][j]
for i in range(N):
    print(*c[i])