t = int(input())
for _ in range(t):
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]

    a.sort()

    second = a[0][1]
    cnt = 1

    for i in a:
        if i[1] < second:
            cnt += 1
            second = i[1]
    print(cnt)