from sys import stdin
n = int(stdin.readline().strip())

sum = 0
for i in range(1, n+1):
    sum += i

print(sum)