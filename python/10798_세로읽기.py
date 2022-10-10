string = []

for i in range(5):
    string.append(list(input()))


for i in range(len(string)):
    for j in range(len(string[i])):
        for k in range(len(string)):
            try:
                print(string[k][j], end='')
            except IndexError:
                print(end='')
    break