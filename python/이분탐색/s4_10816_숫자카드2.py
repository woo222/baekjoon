n = int(input())
num_card = list(map(int, input().split()))
m = int(input())
find_num = list(map(int, input().split()))

num_card.sort()

def bin_start(find):
    left = 0
    right = n-1
    while left <= right:
        idx = (left+right) // 2

        if num_card[idx] >= find:
            right = idx - 1
        elif num_card[idx] < find:
            left = idx + 1

    return left

def bin_end(find):
    left = 0
    right = n-1
    while left <= right:
        idx = (left+right) // 2

        if num_card[idx] > find:
            right = idx - 1
        elif num_card[idx] <= find:
            left = idx + 1

    return right


for num in find_num:
    start = bin_start(num)
    end = bin_end(num)

    print(end - start + 1, end=' ')