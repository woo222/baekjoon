H, M = map(int, input().split())

H *= 60
M += H
M -= 45

if(M < 45):
    M += (24*60)

h = M//60
m = M%60

if(h == 24):
    h = 0
    
print(h, m)