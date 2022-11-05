H, M = map(int, input().split())
time = int(input())

M += (H * 60) + time

h = M//60
m = M%60

if(h >= 24):
    h -= 24
    
print(h, m)