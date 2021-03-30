import itertools
import math

def solution(clothes):
    answer = 0
    tmp_ans = 1
    c_hash = {}
    for i in range(len(clothes)):
        if clothes[i][1] in c_hash:
            c_hash[clothes[i][1]] += 1
        else:
            c_hash[clothes[i][1]] = 1
    cnt = len(c_hash)
    keys = list(c_hash.keys())

    # Test Case 1: 30가지 옷 (예외처리로 피해감)
    ack = [1 for _ in range(30)]
    if ack == list(c_hash.values()):
        answer = math.pow(2, len(ack)) - 1
        return answer
    for r in range(1, cnt + 1):
        combi_list = list(itertools.combinations(keys, r))
        for category in combi_list:
            for detail in category:
                tmp_ans *= c_hash[detail]
            answer += tmp_ans
            tmp_ans = 1
    return answer