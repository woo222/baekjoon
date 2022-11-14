char = input()
cList = []
char.upper()
max = 0

for c in char:
    if(c not in cList):
        cList.append(c)
    
for c in cList:
    if(max < char.count(c)):
        if(max == char.count(c)):
            rst = '?'
            break
        max = char.count(c)
        rst = c
    
        

print(rst)