from collections import deque

n = int(input())
card = deque([i for i in range(1, n+1)])

while(len(card) > 1):
    card.popleft()
    card.append(card.popleft())

print(card[0])

'''
n이 5일 때 
card[0]제거하고 card[1]을 맨뒤card[5]로 옮기고
card[2]제거하고, card[3]을 card[6]으로 옮기고
card[4]제거 card[5] 를[7]로
card[6]제거 card[7] 남음

card[0]제거하고 card[1]을 맨뒤card[5]로 옮기고
card[2]제거하고, card[3]을 card[6]으로 옮기고
card[4]제거 card[5]=[1] 를[7]로
card[6]=[3]제거 card[7]=[1] 남음 


n 이 6
card[0]제거하고 card[1]을 맨뒤card[6]로 옮기고
card[2]제거하고, card[3]을 card[7]으로 옮기고
card[4]제거 card[5] 를[8]로
card[6]제거 card[7] 를[9]로
card[8]제거 card[9]남음


python에서 del 0을 해버리면 맨 앞에 것이 삭제가 되고 자동으로 인덱스가 당겨짐
append로 맨 뒤에 추가

n = int(input())
card = []

for i in range(1, n+1):
    card.append(i)

while True:
    # card의 값이 1만 남으면 끝내기
    if(len(card) == 1):
        break

    del card[0]
    card.append(card.pop(0))

print(card[0])
'''