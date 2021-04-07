import heapq

def solution(jobs):
    cnt, ll, answer = 0, -1, 0
    heap = []
    jobs.sort()
    time = jobs[0][0]
    while cnt < len(jobs):
        for s, t in jobs:
            if ll < s <= time:
                heapq.heappush(heap, (t, s))
        if len(heap) > 0:
            cnt += 1
            ll = time
            duration, start = heapq.heappop(heap)
            time += duration
            answer += (time - start)
        else:
            time += 1
    return answer//len(jobs)