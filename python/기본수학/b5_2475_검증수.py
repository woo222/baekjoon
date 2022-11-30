num = list(map(int, input().split()))
sum = 0
for n in num:
    sum += pow(n, 2)

print(sum%10)