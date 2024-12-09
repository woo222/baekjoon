'''
회문 - 0
유사 회문 - 1
그 외 - 2
'''
def is_word(word):
    return word == word[::-1]

n = int(input())

for _ in range(n):
    word = input()

    if (is_word(word)):
        print(0)
        continue

    result = False
    left = 0
    right = len(word)-1

    while (left < right):
        # 불일치 한 번으로 판별
        if(word[left] != word[right]):
            r_left = word[left+1:right+1]
            r_right = word[left:right]
            result =  is_word(r_left) or is_word(r_right)
            break

        left += 1
        right -= 1

    
    if result:
        print(1)
    else:
        print(2)