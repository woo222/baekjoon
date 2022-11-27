n, m = map(int, input().split())
tree = list(map(int, input().split()))

start = 1
end = max(tree)

while(start <= end):
    mid = (start + end) // 2

    cut_num = 0

    for i in tree:
        if i >= mid:
            cut_num += (i - mid)

    if cut_num >= m:
        start = mid + 1
    elif cut_num < m:
        end = mid -1

print(end)