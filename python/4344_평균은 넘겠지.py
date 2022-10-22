n = int(input())

for i in range(n):
    sum = 0
    count = 0
    score = list(map(int, input().split()))
    score = list(map(int, input().split()))

    for j in range(score[0]):
        sum += score[j+1]
        
    avg = sum / score[0]

    for j in range(score[0]):
        if(score[j+1] > avg):
            count += 1

    result = count / score[0] * 100

    print("{:.3f}%".format(result))
