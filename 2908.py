A, B = map(str, input().split())
num_list = []
num_list.append(int(A[::-1]))
num_list.append(int(B[::-1]))
print(max(num_list))