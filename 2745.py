N, B = map(str, input().split())
B = int(B)

arr = []

for i in range(len(N)):
    try:
        arr.append(int(N[i]))
    except:
        if N[i] == 'A':
            arr.append(10)
        elif N[i] == 'B':
            arr.append(11)
        elif N[i] == 'C':
            arr.append(12)
        elif N[i] == 'D':
            arr.append(13)
        elif N[i] == 'E':
            arr.append(14)
        elif N[i] == 'F':
            arr.append(15)
        elif N[i] == 'G':
            arr.append(16)
        elif N[i] == 'H':
            arr.append(17)
        elif N[i] == 'I':
            arr.append(18)
        elif N[i] == 'J':
            arr.append(19)
        elif N[i] == 'K':
            arr.append(20)
        elif N[i] == 'L':
            arr.append(21)
        elif N[i] == 'M':
            arr.append(22)
        elif N[i] == 'N':
            arr.append(23)
        elif N[i] == 'O':
            arr.append(24)
        elif N[i] == 'P':
            arr.append(25)
        elif N[i] == 'Q':
            arr.append(26)
        elif N[i] == 'R':
            arr.append(27)
        elif N[i] == 'S':
            arr.append(28)
        elif N[i] == 'T':
            arr.append(29)
        elif N[i] == 'U':
            arr.append(30)
        elif N[i] == 'V':
            arr.append(31)
        elif N[i] == 'W':
            arr.append(32)
        elif N[i] == 'X':
            arr.append(33)
        elif N[i] == 'Y':
            arr.append(34)
        elif N[i] == 'Z':
            arr.append(35)
            
arr = arr[::-1]
sum = 0
for i in range(len(arr)):
    sum += arr[i] * (B ** i)

print(sum)