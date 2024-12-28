from sys import stdin

total = int(stdin.readline().strip())
n = int(stdin.readline().strip())

sum = 0
for _ in range(n):
    price, num = map(int, stdin.readline().split())

    sum += price * num

if total == sum:
    print("Yes")
else:
    print("No")