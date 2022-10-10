n = []
string = [[None for i in range(5)]for j in range(15)]

for i in range(5):
    n.append(list(input()))

for i in range(len(n)):
    for j in range(len(n[i])):
        string[j][i] = n[i][j]

for i in string:
    for j in i:
        if j != None:
            print(j, end='')
        else:
            print(end='')