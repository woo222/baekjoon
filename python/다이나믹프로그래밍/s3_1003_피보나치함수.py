t = int(input())
for _ in range(t):
    zero = 1
    one = 0

    n = int(input())
    for i in range(n):
        zero, one = one, zero + one
    print(zero, one)