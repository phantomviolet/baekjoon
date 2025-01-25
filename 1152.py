S = str(input())

j = 0
count = 0
word_count = 0
for i in range(len(S)):
    if S[i] != ' ':
        count += 1
    elif S[i] == ' ' and count > 0:
        word_count += 1
        count = 0
if count > 0:
    word_count += 1
print(word_count)  