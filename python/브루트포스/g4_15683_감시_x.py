cctv_map = []
n, m = map(int, input().split())

for i in range(n):
    cctv_map.append(list(map(str, input().split())))

for i in range(n):
    for j in range(m):
        if(cctv_map[i][j] == '1'):
            cctv_map