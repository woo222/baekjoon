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
            break

'''
또 다른 방법
string = []
number = []

for i in range(5):
    string.append(list(input()))
    number.append(len(string[i]))


for i in range(max(number)):
    for j in range(len(string)):
        try:
            print(string[j][i], end='')
        except IndexError:
            print(end='')
'''