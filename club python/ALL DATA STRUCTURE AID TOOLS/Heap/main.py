# https://docs.python.org/3/library/heapq.html
import heapq
from typing import List
# https://pypi.org/project/heapq_max/
from heapq_max import *

'''
    Link: https://leetcode.com/problems/k-closest-points-to-origin/
    Purpose: Find the k closest points to the origin (0, 0). Answer can be in any order.
    parameter: List[List[int]] points - a list of x- and y-coordinate integer
             : int k - a number of the closet points ti the integer to find
    return: List[List[int]] answer - the k closest points to the origin (0, 0)
    Pre-Condition: 1 <= k <= points.length <= 10^4
                 : -10^4 < xi, yi < 10^4
    Post-Condition: none
'''
# sorting solution: runtime: O(nlog(n)), memory: O(n)
def kClosest_M1(points: List[List[int]], k: int) -> List[List[int]]:
    distanceAndPoints = []
    for point in points:
        y = point[1]
        x = point[0]
        distance = x * x + y * y
        distanceAndPoints.append([distance, point])

    distanceAndPoints.sort()
    answer = []
    for i in range(k):
        answer.append(distanceAndPoints[i][1])

    return answer

'''
    Link: https://leetcode.com/problems/k-closest-points-to-origin/
    Purpose: Find the k closest points to the origin (0, 0). Answer can be in any order.
    parameter: List[List[int]] points - a list of x- and y-coordinate integer
             : int k - a number of the closet points ti the integer to find
    return: List[List[int]] answer - the k closest points to the origin (0, 0)
    Pre-Condition: 1 <= k <= points.length <= 10^4
                 : -10^4 < xi, yi < 10^4
    Post-Condition: none
'''
# min heap solution: runtime: O(nlog(n)), memory: O(n)
def kClosest_M2(points: List[List[int]], k: int) -> List[List[int]]:
    # make a minHeap of a list [distance, [xAxis, yAxis]]
    minHeap = [[points[i][0] * points[i][0] + points[i][1] * points[i][1], points[i]] for i in range(len(points))]

    # sort by using min heap
    heapq.heapify(minHeap)

    # return the first k element in the heap from the root
    return [heapq.heappop(minHeap)[1] for _ in range(k)]

'''
    Link: https://leetcode.com/problems/k-closest-points-to-origin/
    Purpose: Find the k closest points to the origin (0, 0). Answer can be in any order.
    parameter: List[List[int]] points - a list of x- and y-coordinate integer
             : int k - a number of the closet points ti the integer to find
    return: List[List[int]] answer - the k closest points to the origin (0, 0)
    Pre-Condition: 1 <= k <= points.length <= 10^4
                 : -10^4 < xi, yi < 10^4
    Post-Condition: none
'''
# max heap solution: runtime: O(nlog(k)), memory: O(k) where k is a number of needed smallest numbers
def kClosest_M3(points: List[List[int]], k: int) -> List[List[int]]:
    # make a maxheap of a list by inversting distances because direct maxHeap doesn't support by the heapq library [-distance, [xAxis, yAxis]]
    maxHeap = [[-(points[i][0] * points[i][0] + points[i][1] * points[i][1]), points[i]] for i in range(k)]

    heapq.heapify(maxHeap)

    # compare current distance with the largest distance (-smallest_number) in a heap
    for i in range(k, len(points)):
        x = points[i][0]
        y = points[i][1]
        distance = -(x * x + y * y)
        if distance > maxHeap[0][0]:
            heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, [distance, points[i]])

    # return only [x-axis, y-axis]
    return [[point[1][0], point[1][1]] for point in maxHeap]

'''
    Link: https://leetcode.com/problems/k-closest-points-to-origin/
    Purpose: Find the k closest points to the origin (0, 0). Answer can be in any order.
    parameter: List[List[int]] points - a list of x- and y-coordinate integer
             : int k - a number of the closet points ti the integer to find
    return: List[List[int]] answer - the k closest points to the origin (0, 0)
    Pre-Condition: 1 <= k <= points.length <= 10^4
                 : -10^4 < xi, yi < 10^4
    Post-Condition: none
'''
# max heap solution: runtime: O(nlog(k)), memory: O(k) where k is a number of needed smallest numbers
def kClosest_M4(points: List[List[int]], k: int) -> List[List[int]]:
    # make a maxheap of a list [-distance, [xAxis, yAxis]]
    maxHeap = [[points[i][0] * points[i][0] + points[i][1] * points[i][1], points[i]] for i in range(k)]

    heapify_max(maxHeap)

    # compare current distance with the largest distance (-smallest_number) in a heap
    for i in range(k, len(points)):
        x = points[i][0]
        y = points[i][1]
        distance = x * x + y * y
        if distance < maxHeap[0][0]:
            heappop_max(maxHeap)
            heappush_max(maxHeap, [distance, points[i]])

    # return only [x-axis, y-axis]
    return [[point[1][0], point[1][1]] for point in maxHeap]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n+===== solution 1: sorting ====+\n")
    print(kClosest_M1(points=[[1,3],[-2,2]], k = 1)) # [[-2, 2]]
    print(kClosest_M1(points = [[3,3],[5,-1],[-2,4]], k = 2)) # [[3, 3], [-2, 4]]
    print(kClosest_M1(points=[[0, 1], [1, 0]], k=2)) # [[0, 1], [1, 0]]
    print(kClosest_M1(points=[[1, 3], [-2, 2], [0, 0], [-5, -5]], k=3)) # [[0, 0], [-2, 2], [1, 3]]
    print(kClosest_M1(points=[[68,97],[34,-84],[60,100],[2,31],[-27,-38],[-73,-74],[-55,-39],[62,91],[62,92],[-57,-67]],k=5))  # [[[2,31],[-27,-38],[-55,-39],[-57,-67],[34,-84]]]

    print("\n+===== solution 2: Min Heap ====+\n")

    print(kClosest_M2(points=[[1, 3], [-2, 2]], k=1))  # [[-2, 2]]
    print(kClosest_M2(points=[[3, 3], [5, -1], [-2, 4]], k=2))  # [[3, 3], [-2, 4]]
    print(kClosest_M2(points=[[0, 1], [1, 0]], k=2))  # [[0, 1], [1, 0]]
    print(kClosest_M2(points=[[1, 3], [-2, 2], [0, 0], [-5, -5]], k=3))  # [[0, 0], [-2, 2], [1, 3]]
    print(kClosest_M2(
        points=[[68, 97], [34, -84], [60, 100], [2, 31], [-27, -38], [-73, -74], [-55, -39], [62, 91], [62, 92],
                [-57, -67]], k=5))  # [[[2,31],[-27,-38],[-55,-39],[-57,-67],[34,-84]]]

    print("\n+===== solution 3: Max Heap V_1 ====+\n")

    print(kClosest_M3(points=[[1, 3], [-2, 2]], k=1))  # [[-2, 2]]
    print(kClosest_M3(points=[[3, 3], [5, -1], [-2, 4]], k=2))  # [[3, 3], [-2, 4]]
    print(kClosest_M3(points=[[0, 1], [1, 0]], k=2))  # [[0, 1], [1, 0]]
    print(kClosest_M3(points=[[1, 3], [-2, 2], [0, 0], [-5, -5]], k=3))  # [[0, 0], [-2, 2], [1, 3]]
    print(kClosest_M3(
        points=[[68, 97], [34, -84], [60, 100], [2, 31], [-27, -38], [-73, -74], [-55, -39], [62, 91], [62, 92],
                [-57, -67]], k=5))  # [[[2,31],[-27,-38],[-55,-39],[-57,-67],[34,-84]]]

    print("\n+===== solution 4: Max Heap V_2 ====+\n")

    print(kClosest_M4(points=[[1, 3], [-2, 2]], k=1))  # [[-2, 2]]
    print(kClosest_M4(points=[[3, 3], [5, -1], [-2, 4]], k=2))  # [[3, 3], [-2, 4]]
    print(kClosest_M4(points=[[0, 1], [1, 0]], k=2))  # [[0, 1], [1, 0]]
    print(kClosest_M4(points=[[1, 3], [-2, 2], [0, 0], [-5, -5]], k=3))  # [[0, 0], [-2, 2], [1, 3]]
    print(kClosest_M4(
        points=[[68, 97], [34, -84], [60, 100], [2, 31], [-27, -38], [-73, -74], [-55, -39], [62, 91], [62, 92],
                [-57, -67]], k=5))  # [[[2,31],[-27,-38],[-55,-39],[-57,-67],[34,-84]]]
