from collections import deque

def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    total_weight = 0
    time = 0
    # running_bridge: 현재 다리 위 지나는 차량 큐
    running_bridge = deque(0 for _ in range(bridge_length))

    while (len(running_bridge) != 0):
        # out: 다리에서 나가는 차량
        out = running_bridge.popleft()
        total_weight -= out
        time += 1
        # 대기 챠량이 모두 나가면 이 코드 블럭 실행 안함
        if truck_weights:
            # 다리에 올라오는 경우
            if truck_weights[0] + total_weight <= weight:
                in_ = truck_weights.popleft()
                running_bridge.append(in_)
                total_weight += in_
            else:
                running_bridge.append(0)

    answer = time
    return answer
