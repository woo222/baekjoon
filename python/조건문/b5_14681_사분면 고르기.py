from sys import stdin

x = int(stdin.readline().strip())
y = int(stdin.readline().strip())

if x > 0:
    if y > 0:
        print(1)
    else:
        print(4)

else:
    if y > 0:
        print(2)
    else:
        print(3)