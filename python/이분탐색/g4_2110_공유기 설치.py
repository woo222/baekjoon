n, c = map(int, input().split())
house = [int(input()) for _ in range(n)]
house.sort()

start = 1
end = house[-1] - house[0]
length = 0

while (start <= end):
    mid = (start + end) // 2
    cnt = 1
    a = house[0]
    for i in range(1, n):
        if(house[i] >= a + mid):
            a = house[i]
            cnt += 1

    if(cnt >= c):
        start = mid + 1
        length = mid
    else:
        end = mid - 1

print(length)