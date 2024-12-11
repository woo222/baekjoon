a_str = input()
b_str = input()
result = [[0]*(len(b_str)+1)  for _ in range(len(a_str)+1)]

for i in range(len(a_str)):
    for j in range(len(b_str)):
        if a_str[i] == b_str[j]:
            result[i+1][j+1] = result[i][j] + 1
        else:
            result[i+1][j+1] = max(result[i][j+1], result[i+1][j])

        
print(max(max(result)))