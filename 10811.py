N, M = map(int, input().split())
location1 = []
location2 = []
basket = [i for i in range(1, N+1)]

for i in range(M):
    num1, num2 = map(int, input().split())
    location1.append(num1)
    location2.append(num2)
    
def reversed_by_range(start_point, end_point, basket):
    if start_point == end_point:
        return basket
    tmp_list = []
    tmp_list = basket[start_point - 1 : end_point]
    tmp_list.reverse()
    
    basket[start_point - 1 : end_point] = tmp_list
    return basket

for i in range(M):
    basket = reversed_by_range(location1[i], location2[i], basket)
    
for i in range(len(basket)):
    print(basket[i], end=' ')
    
