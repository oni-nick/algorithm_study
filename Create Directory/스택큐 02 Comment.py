def solution(prices):
    answer = [0 for _ in range(len(prices))]

    for i in range(len(prices)):
        for j in range(i+1, len(prices)):   # i번째 요소는 i+1번째 요소부터 비교 시작함.
            if prices[i] > prices[j]:       # 가격이 떨어진다면, 1초뒤에 떨어지므로 1초를 더해주고 break (가격이 떨어진 이후 다시 오르더라도 결과에 반영하지 않음)
                answer[i] += 1
                break
            else:
                answer[i] += 1
    return answer

