n = int(input())
num = list(map(int, input().split()))
find_n = int(input())
cnt = 0
result = 0

for i in num:
    cnt += 1
    if (cnt > n):
        break

    if (i == find_n):
        result += 1

print(result)