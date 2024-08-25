num = int(input())
arr = [int(input()) for _ in range(num)]
result = [0 for _ in range(num)]

if (len(arr) <=2):
    print(sum(arr))
else:
    result[0] = arr[0]
    result[1] = max(arr[0]+arr[1], arr[1])
    for i in range(2, num):
        result[i] = max(result[i-3]+arr[i-1]+arr[i], result[i-2]+arr[i])

    print(result[-1])