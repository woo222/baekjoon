m, n = map(int, input().split())
snack = list(map(int, input().split()))

start = 1
end = max(snack)

while(start <= end):
    cnt = 0
    mid = (start + end) // 2

    for i in snack:
        if(i >= mid):
            cnt += i // mid

    if (cnt >= m):
        start = mid + 1
    else:
        end = mid - 1

print(end)