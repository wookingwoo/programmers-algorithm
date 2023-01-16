# Level 2
import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    n = 0

    while (True):
        if len(scoville) == 1 and scoville[0] < K:
            return -1

        m1 = heapq.heappop(scoville)

        if m1 >= K:
            return n
        else:
            m2 = heapq.heappop(scoville)
            heapq.heappush(scoville, m1 + (m2 * 2))
            n += 1


print(solution([1, 2, 3, 9, 10, 12], 7))  # 2
