n = int(input())
tmp_list = []
for i in range(n):
    tmp_list.append(str(input()))
for i in range(n):
    tmp_str = tmp_list[i]
    print(tmp_str[0], tmp_str[-1], sep = "")