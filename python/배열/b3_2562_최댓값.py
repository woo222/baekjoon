max = 0
loc = 0
for i in range(9):
    a = int(input())

    if (max < a):
        max = a
        loc = i+1

print(max)
print(loc)