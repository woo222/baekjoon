'''
배열의 인덱스는 행, 값은 열
같은 행: 인덱스로 표시 되면서 중복이 허용되지 않으므로 고려x
같은 열: 배열의 값이 같은 경우
같은 대각선: 두 인덱스의 차이와 해당하는 두 값의 차이의 절대값이 같은 경우
'''
n = int(input())
map_queen = [0] * n
result = 0

def n_queen(x):
    global result
    if x == n:
        result += 1
        return
    else:
        for i in range(n):
            map_queen[x] = i
            if bool_queen(x):
                n_queen(x+1)

def bool_queen(x):
    # 같은 열 & 같은 대각선 확인
    for i in range(x):
        if map_queen[i] == map_queen[x] or abs(map_queen[i] - map_queen[x]) == abs(i - x):
            return False
    return True

n_queen(0)
print(result)