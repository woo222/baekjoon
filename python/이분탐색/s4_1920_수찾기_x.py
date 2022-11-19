n = int(input())
example = list(map(int, input().split()))
m = int(input())
answer = list(map(int, input().split()))

example.sort()

def bin (quest):
    left = 0
    right = n - 1

    while left <= right:
        find = (left + right)//2

        if(example[find] == quest):
            return True
        
        if(example[find] > quest):
            right = find - 1
        elif(example[find] < quest):
            left = find + 1
        

for i in range(m):
    if (bin(answer[i])):
        print(1)
    else:
        print(0)
