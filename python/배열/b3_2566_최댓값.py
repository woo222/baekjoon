max = -1
x = y = 0
for i in range(9):
    number = list(map(int, input().split()))

    cnt = 0
    for num in number:
        cnt += 1
        if ( max < num ):
            max = num
            x = i + 1
            y = cnt

print(max)
print(x, y)