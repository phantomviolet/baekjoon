king, queen, rook, bishop, knight, pawn = map(int, input().split())
new_list = []
new_list.append(king - 1)
new_list.append(queen - 1)
new_list.append(rook - 2)
new_list.append(bishop - 2)
new_list.append(knight - 2)
new_list.append(pawn - 8)

for i in range(len(new_list)):
    print(new_list[i] * -1, end=' ')