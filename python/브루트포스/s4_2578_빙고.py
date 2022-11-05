bingo = []
loc = 0

for i in range(5):
  bingo.append(list(map(int, input().split())))
  
for i in range(5):
  call = list(map(int, input().split()))
  
  for j in range(5):
    count = 0
    loc += 1
    
    for k in range(5):
      for l in range(5):
        if(bingo[k][l] == call[j]):
          bingo[k][l] = -1

    # 가로 줄 빙고
    for k in range(5):
      if(sum(bingo[k]) == -5):
        count += 1
      
    # 세로 줄 빙고
    for k in range(5):
      yCount = 0
      for l in range(5):
        if(bingo[l][k] == -1):
          yCount += 1
      if(yCount == 5):
        count += 1

    # 대각선 빙고
    if(bingo[0][0]+bingo[1][1]+bingo[2][2]+bingo[3][3]+bingo[4][4]==-5) or (bingo[0][-1]+bingo[1][-2]+bingo[2][-3]+bingo[3][-4]+bingo[4][-5]==-5):
      count += 1

    if(count >= 3):
      print(loc)
      exit()