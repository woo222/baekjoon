# 1~26만 사용가능 27이상은 끊을수 없음
# 최대로 끊을 수 있는 것이 2개
# 최소 1개
# 1개씩 끊거나 2개씩 끊거나
# 재귀를 사용하면 시간초과
# 자리 수를 이용해서 count 값으로 계산


num = list(map(int, input()))
nLlist = [0 for _ in range(len(num)+1)]
# 암호 해석 못하는 경우
if(num[0] == 0):
    print(0)
# 암호 해석 가지 수 구하기
else:
    # 0번째와 1번짼 구할 수 있는 암호가 1가지 수
    nLlist[0] = nLlist[1] = 1
    # 입력받은 숫자의 두번째 자리 부터 확인
    for i in range (2, len(num)+1):
        # 지금 확인 하고 있는 숫자가 (1의 자리) 자연수인 경우
        if (num[i-1] > 0):
            # 지금 확인 하는 숫자를 한 자리 수로 그냥 붙일 수 있기 때문에 이전에 구한 가지 수 그대로 가져옴
            nLlist[i] += nLlist[i-1]
        # 1의 자리와 앞의 자리 수 계산하기
        tmp = num[i-2] * 10 + num[i-1]
        # 알파벳으로 변환이 가능한 두 자리 수 인지 확인
        if (tmp >= 10 and tmp <= 26):
            # 숫자 2개를 하나로 인식하여 두 단계 전에 구한 계산 결과 더하기
            nLlist[i] += nLlist[i-2]
    print(nLlist[len(num)] % 1000000)