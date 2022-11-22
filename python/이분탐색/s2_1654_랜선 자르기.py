k, n = map(int, input().split())
a = [int(input()) for i in range(k)]

start = 1
end = max(a)

while(start <= end):
    mid = (start + end) // 2

    num = 0

    for i in a:
        num += i // mid

    if num >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)