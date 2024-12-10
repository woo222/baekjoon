t = int(input())

for _ in range(t):
    word = input()
    k = int(input())

    # 문자 개수 세기
    count_w = {}
    for w in word:
        count_w[w] = count_w.get(w, 0) + 1

    # 인덱스 저장
    check = False
    check_index = {}
    max_result = 0
    min_result = len(word)
    
    # k개 이하인 경우 제외
    for i in range(len(word)):
        if count_w[word[i]] < k:
            continue

        # 포함하는 단어 찾기
        check = True
        check_index[word[i]] = check_index.get(word[i], []) + [i]

    # 최대 최소 찾기
    for key, value in check_index.items():
        for i in range(len(value)-k +1):
            max_result = max(max_result, value[i+k-1] - value[i] + 1)
            min_result = min(min_result, value[i+k-1] - value[i] + 1)

    if (check):
        print(min_result, max_result)
    else:
        print(-1)