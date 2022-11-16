n = int(input())

num = list(map(int, input().split()))

for i in range(len(num)):
    if(i >= n):
        num.pop()

print(min(num), max(num))