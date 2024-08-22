a = int(input())
t = int(input())
answer = int(input())
count = 0
j = 1
person = 0

while(True):
    game = sum([[0],[1],[0],[1],[0 for k in range(j+1)],[1 for k in range(j+1)]],[])
    for p in game:
        if (p == answer):
            count += 1

        if (count == t):
            print(person % a)
            exit(0)
            
        person += 1
        
    j+=1