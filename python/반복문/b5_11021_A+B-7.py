from sys import stdin

t = int(stdin.readline().strip())

for i in range(1, t+1):
    a, b = map(int, stdin.readline().split())

    print("Case #" +  str(i) + ":", a+b)