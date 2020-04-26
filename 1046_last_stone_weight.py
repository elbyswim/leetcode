import heapq

def lastStoneWeight(stones):
    stones = [-stone for stone in stones]
    heapq.heapify(stones)
    while len(stones) > 1:
        x = heapq.heappop(stones)
        y = heapq.heappop(stones)
        if x < y:
            heapq.heappush(stones, x - y)
    if len(stones) < 1:
        return 1
    return -stones[0]


print(lastStoneWeight([1]))
