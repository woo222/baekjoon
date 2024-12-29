from sys import stdin
import math

n, m = map(int, stdin.readline().split())

number = []
result = -1

for _ in range(n):
    number.append(stdin.readline().strip())

for i in range(n):
    for j in range(m):
        for xd in range(-n, n):
            for yd in range(-m, m):
                s = ""
                x, y = i, j
                if xd == 0 and yd == 0:
                    continue
                while 0 <= x < n and 0 <= y < m:
                    s += number[x][y]
                    if int(math.sqrt(int(s))) ** 2 == int(s):
                        result = max(result, int(s))
                    x += xd
                    y += yd
print(result)