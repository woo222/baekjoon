import math

t = int(input())

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

    if d == 0:
        # 무수히 많은 경우
        if r1 == r2:
            print(-1)
        # 접점이 없는 경우
        else:
            print(0)
    else:
        if (r1 + r2 == d) or (abs(r1-r2) == d):
            print(1)
        elif (r1 + r2 > d) and (d > abs(r1 - r2)):
            print(2)
        else:
            print(0)