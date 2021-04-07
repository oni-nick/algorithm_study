import heapq
def solution(scoville, K):
    heap = []
    answer = 0
    new = 0
    for i in scoville:
        heapq.heappush(heap, i)
    while(heap[0] <= K):
        if len(heap) > 1:
            low1 = heapq.heappop(heap)
            low2 = heapq.heappop(heap)
            new = low1 + (low2 * 2)
            heapq.heappush(heap, new)
            answer += 1
        else:
            return -1
    return answer
