import heapq
import math

'''
    Purpose: Determine the minimum total weight after d days, where each day a weight in weights will be reduced by a half.
    parameter: List[int] weight - a list of weights
             : int d: - a number of days
    return: int - the minimum total weight after d days
    Pre-Condition: 1 <= weights <= 10^4
                 : 1 <= weights[i] <= 100
                 : 1 <= d <= 100
    Post-Condition: none
'''
# max heap: runtime: O(d), space: O(n)
def minimumTotalWeight(weights, d):
    max_heap = [-w for w in weights]
    heapq.heapify(max_heap)

    for _ in range(d):
        heaviest_weight = -heapq.heappop(max_heap)
        remaining = math.floor(heaviest_weight / 2)
        heapq.heappush(max_heap, -remaining)

    return -sum(max_heap)

if __name__ == '__main__':
    print(minimumTotalWeight([30, 20, 25], 4)) # 29
    print(minimumTotalWeight([30, 20, 25], 0))  # 75
    print(minimumTotalWeight([30, 20, 25], 1))  # 60
    print(minimumTotalWeight([1, 10, 2], 3))  # 4
    print(minimumTotalWeight([10, 10, 10], 100))  # 0