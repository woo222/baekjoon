def boyerMoore(arr):
    count = 0
    major = 0
    for i in arr:
        if count == 0:
            major = i
        if major == i:
            count += 1
        else:
            count -= 1

    k = len(arr)
    m = 0
    for i in arr:
        if i == major:
            m += 1
    if m > k//2:
        return major
    else:
        return "SYJKGW"

n = int(input())

for i in range(n):
    t = list(map(int, input().split()))
    print(boyerMoore(t[1:]))