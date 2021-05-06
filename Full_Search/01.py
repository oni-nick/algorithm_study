def solution(answers):
    answer = []
    cnt = [0, 0, 0]
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    sss = [s1, s2, s3]
    for i in range(3):
        if len(answers) <= len(sss[i]):
            sss[i] = sss[i][:len(answers)]
        else:
            sss[i] = sss[i] * (len(answers) // len(sss[i]) + 1)  # 리스트 확장
            sss[i] = sss[i][:len(answers)]

    for i in range(len(answers)):
        if answers[i] == sss[0][i]:
            cnt[0] += 1
        if answers[i] == sss[1][i]:
            cnt[1] += 1
        if answers[i] == sss[2][i]:
            cnt[2] += 1

    max_ = max(cnt)
    for i in range(3):
        if max_ == cnt[i]:
            answer.append(i + 1)
    return answer
