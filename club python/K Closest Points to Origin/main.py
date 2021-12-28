from typing import List
import heapq

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
# min heap solution: runtime: O(n), memory: O(n)
def kClosest_M2(points: List[List[int]], k: int) -> List[List[int]]:
    # make a minHeap of a list [distance, [xAxis, yAxis]]
    minHeap = [[points[i][0] * points[i][0] + points[i][1] * points[i][1], points[i]] for i in range(len(points))]
    heapq.heapify(minHeap)

    # return the first k element in the heap from the root
    answer = [heapq.heappop(minHeap)[1] for _ in range(k)]

    return answer

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n+===== solution 1: sorting ====+\n")
    print(kClosest_M1(points=[[1,3],[-2,2]], k = 1)) # [[-2, 2]]
    print(kClosest_M1(points = [[3,3],[5,-1],[-2,4]], k = 2)) # [[3, 3], [-2, 4]]
    print(kClosest_M1(points=[[0, 1], [1, 0]], k=2)) # [[0, 1], [1, 0]]
    print(kClosest_M1(points=[[1, 3], [-2, 2], [0, 0], [-5, -5]], k=3)) # [[0, 0], [-2, 2], [1, 3]]
    print(kClosest_M1(points=[[1, 3], [-2, 2]], k=0)) # []
    print(kClosest_M1(points=[[68,97],[34,-84],[60,100],[2,31],[-27,-38],[-73,-74],[-55,-39],[62,91],[62,92],[-57,-67]],k=5))  # [[[2,31],[-27,-38],[-55,-39],[-57,-67],[34,-84]]]

    print("\n+===== solution 2: Min Heap ====+\n")

    print(kClosest_M2(points=[[1, 3], [-2, 2]], k=1))  # [[-2, 2]]
    print(kClosest_M2(points=[[3, 3], [5, -1], [-2, 4]], k=2))  # [[3, 3], [-2, 4]]
    print(kClosest_M2(points=[[0, 1], [1, 0]], k=2))  # [[0, 1], [1, 0]]
    print(kClosest_M2(points=[[1, 3], [-2, 2], [0, 0], [-5, -5]], k=3))  # [[0, 0], [-2, 2], [1, 3]]
    print(kClosest_M2(points=[[1, 3], [-2, 2]], k=0))  # []
    print(kClosest_M2(
        points=[[68, 97], [34, -84], [60, 100], [2, 31], [-27, -38], [-73, -74], [-55, -39], [62, 91], [62, 92],
                [-57, -67]], k=5))  # [[[2,31],[-27,-38],[-55,-39],[-57,-67],[34,-84]]]
