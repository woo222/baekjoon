'''
판 수, 지뢰 수
지뢰 좌표 (1부터 시작)
UP, LEFT, RIGHT 만 가능
4 4
1 3
2 2
4 4
2 3
'''

n, m = map(int, input().split())
x_loc = []
y_loc = []

for i in range(m):
    x, y = map(int, input().split())
    x_loc.append(x)
    y_loc.append(y)
if (n-min(y_loc) >= max(y_loc)-1):
    r = max(y_loc)-1
else:
    r = n-min(y_loc)
print(max(x_loc)-1 + r)

# 가장 아래 위치한 지뢰 위치에서 -1 한 값을 rst 에 더하고
# 왼쪽 오른쪽 비교해서 (n- loc[][1]이 가장 작은 지뢰값) (loc[][0]중 가장 큰 지뢰값-1) 둘 중 더 작은 값을 rst에 더함
# print(rst)