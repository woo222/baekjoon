n = int(input())

num = list(map(int, input().split()))
min = max = num[0]

for j in range(n):
    if(num[j] < min):
        min = num[j]
    if(num[j] > max):
        max = num[j]
print(min, max)