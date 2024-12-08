l = int(input())
string = input()
global patternHash
global pattern

def patterHashMaker(length, cursor):
    pattern = string[cursor:cursor+length]
    if (cursor == 0):
        power = 1
        patternHash = 0
        for i in range(length):
            patternHash += pattern[length-1-i]*power
            if(i<length-1):
                power = power * 2

    else:
        patternHash = 2 * (patternHash - string[cursor-1] * pow(2, length-1)) + string[length - 1 + cursor]


def patternCheck(length):
    for i in range(l-length):
        patterHashMaker(length, i)
        cnt = 0

        for j in range(l-length):
            subString = string[j:j+length]
            if (j==0):
                subStringHash = 0
                power = 1
                for k in range(length):
                    subStringHash += string[length-1-k]*power
                    if(k < length-1):
                        power = power*2
            else:
                subStringHash = 2 * (subStringHash - string[j-1]*pow(2,length-1)) + string[length-1+j]

            if (subStringHash == patternHash):
                if(subString == pattern):
                    cnt += 1
            if (cnt >= 2):
                return True
    return False


left = 0
right = l
while(left < right):
    mid = (left + right) / 2

    if (patternCheck(mid)):
        left = mid + 1
        answer = mid
    else:
        right = mid
print(answer)
    