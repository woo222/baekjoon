board = []
baduk = []

for i in range(19):
    board.append(list(map(int, input().split())))

for i in range(19):
    for j in range(19):
        if(board[i][j] != 0):
            baduk.append([board[i][j], i, j])

count = 0
for i in range(len(baduk)-1):
    
    # 가로 줄이 5개 인지 확인
    
    if(baduk[i][1] == baduk[i+1][1] and baduk[i][2]+1 == baduk[i+1][2]):
        count +=1
        if baduk[i][0] != baduk[i+1][0]:
            count = 0
        
        if count == 4:
            result = [baduk[i][0], baduk[i][1]+1, baduk[i][2]-2]
            break
    else: count = 0
print(baduk)
# 우 대각선 아래
count = 0
for i in range(len(baduk)):
    new_baduk = baduk[i]
    for j in range(len(baduk)):
        if i == j :
            continue
        if(baduk[i][1]+1 == baduk[j][1] and baduk[i][2]+1 == baduk[j][2]):
            count += 1

            
            if(baduk[i][0] != baduk[j][0]):
                count = 0

            if(baduk[i][1]==17 and baduk[j][1] ==18):
                count+=1
    
            if count == 5:
                result = [baduk[i][0], baduk[i][1]-2, baduk[i][2]-2]
                break

print(baduk)
# 좌 대각선 아래
count = 0
for i in range(len(baduk)-1):
    new_baduk = baduk[i]
    for j in range(len(baduk)-1):
        if i == j :
            continue

        if(baduk[i][1]+1 == baduk[j][1] and baduk[i][2]-1 == baduk[j][2]):
            count += 1
            
            if(baduk[i][0] != baduk[j][0]):
                count = 0

            if count == 4:
                result = [baduk[i][0], baduk[i][1]+2, baduk[i][2]]
                break
print(baduk)
baduk.sort(key= lambda x:x[2])
count = 0
for i in range(len(baduk)-1):
    for j in range(len(baduk)-1):
        if i == j:
            continue

        # 세로 줄이 5개 인지 확인
        if(baduk[i][2] == baduk[j][2] and baduk[i][1]+1 == baduk[j][1]):
            count += 1
            
            if baduk[i][0] != baduk[j][0]:
                count = 0
        
            if count == 4:
                result = [baduk[i][0], baduk[i][1]-1, baduk[i][2]+1]
                break
print(baduk)
print(result[0])
print(result[1], result[2])