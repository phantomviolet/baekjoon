N = int(input())

repeat = []
new_str = []

for i in range(N):
    tmp_repeat, tmp_str = map(str, input().split())
    repeat.append(int(tmp_repeat))
    new_str.append(tmp_str)
    
for i in range(N):
    print_str = ''
    for j in new_str[i]:
        print_str = print_str + j*repeat[i]
    print(print_str)
    