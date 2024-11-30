# 메모리 초과
# from itertools import combinations

# n, k = map(int, input().split())
# luv_list = list(map(int, input().split()))
# com_luv_list = list(combinations(luv_list, k))

# result = max(luv_list)

# for i in com_luv_list:
#     if (result > (max(i)-min(i))):
#         result = max(i)-min(i)
    
# print(result)

# 시간 초과
# from itertools import combinations

# n, k = map(int, input().split())
# luv_list = list(map(int, input().split()))

# result = max(luv_list)

# for i in combinations(luv_list, k):
#     result = min(result, max(i)-min(i))
    
# print(result)

n, k = map(int, input().split())
luv_list = list(map(int, input().split()))

luv_list.sort()
result = max(luv_list)

for i in range(n-k+1):
    num = luv_list[i+k-1] - luv_list[i]
    result = min(result, num)
    
print(result)