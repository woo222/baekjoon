from sys import stdin

t = int(stdin.readline().strip())

for _ in range(t):
    a, b = map(int, stdin.readline().split())
    print(a+b)