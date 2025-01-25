S = str(input())
tmp = []
for i in range(97, 123):
    for j in range(len(S)):
        if chr(i) == S[j]:
            tmp.append(j)
            break
        elif j == len(S) - 1:
            tmp.append(-1)
    
for i in range(len(tmp)):
    print(tmp[i], end=' ')