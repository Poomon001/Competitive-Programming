from typing import List

'''
    Link: https://leetcode.com/problems/sum-of-left-leaves/
    Purpose: Find the k closest points to the origin (0, 0)
    parameter: List[List[int]] points - a list of x- and y-coordinate integer
             : int k - a number of the closet points ti the integer to find
    return: List[List[int]] answer - the k closest points to the origin (0, 0)
    Pre-Condition: 1 <= k <= points.length <= 10^4
                 : -10^4 < xi, yi < 10^4
    Post-Condition: none
'''
def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(kClosest(points=[[1,3],[-2,2]], k = 1)) # [[-2, 2]]
    print(kClosest(points = [[3,3],[5,-1],[-2,4]], k = 2)) # [[3, 3], [-2, 4]]
    print(kClosest(points=[[0, 1], [1, 0]], k=2)) # [[0, 1], [1, 0]]
    print(kClosest(points=[[1, 3], [-2, 2], [0, 0], [-5, -5]], k=3)) # [[0, 0], [-2, 2], [1, 3]]
    print(kClosest(points=[[1, 3], [-2, 2]], k=0)) # []
