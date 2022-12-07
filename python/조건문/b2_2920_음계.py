music = list(map(int, input().split()))
rst = 0

for i in range(8):
    if(music[i] == i+1):
        rst = 1
    elif(music[i] == 8-i):
        if(rst == 1):
            rst = 0
            break
        rst = 2
    else:
        rst = 0
        break

if(rst == 1):
    print("ascending")
elif(rst == 2):
    print("descending")
else:
    print("mixed")