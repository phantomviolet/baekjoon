N, M = map(int, input().split())
location1 = []
location2 = []
basket = [i for i in range(1, N+1)]

for i in range(M):
    num1, num2 = map(int, input().split())
    location1.append(num1)
    location2.append(num2)
    
def change(list, l1, l2):
    tmp = list[l1-1]
    list[l1-1] = list[l2-1]
    list[l2-1] = tmp
    return list

for i in range(M):
    basket = change(basket, location1[i], location2[i])
    
for i in range(len(basket)):
    print(basket[i], end=' ')