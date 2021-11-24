from typing import List

'''
    Link: https://leetcode.com/problems/interval-list-intersections/
    Purpose: Determine all overlaps of 2 list of intervals 
    parameter: List[List[int]] firstList - a list of intervals
             : List[List[int]] secondList - a list of intervals
    return: List[List[int]] interval - all overlap between firstInterval and secondInterval  
    Pre-Condition: 0 <= firstList.length, secondList.length <= 1000
                 : firstList.length + secondList.length >= 1
                 : 0 <= starti < endi <= 10^9
                 : endi < starti+1
                 : 0 <= startj < endj <= 10^9
                 : endj < startj+1
    Post-Condition: none
'''
# runtime: O(n), memory: O(1)
def intervalIntersection(firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
    a = 0
    b = 0
    interval = [] # answer doesn't count to memory use

    while (a < len(firstList) and b < len(secondList)):
        # get first interval
        AInterval = firstList[a]
        front1 = AInterval[0]
        back1 = AInterval[1]

        # get second interval
        BInterval = secondList[b]
        front2 = BInterval[0]
        back2 = BInterval[1]

        # part of interval 1 is in interval 2
        if front1 <= front2 and back1 <= back2:
            # check for intersection
            if front2 <= back1:
                interval.append([front2, back1])
            a += 1
        # part of interval 1 is in interval 2
        elif front1 >= front2 and back1 >= back2:
            # check for intersection
            if front1 <= back2:
                interval.append([front1, back2])
            b += 1
        # all interval 2 is in interval 1
        elif front1 <= front2 and back1 >= back2:
            interval.append([front2, back2])
            b += 1
        # all interval 1 is in interval 2
        elif front1 >= front2 and back1 <= back2:
            interval.append([front1, back1])
            a += 1
        # no intersection
        else:
            a += 1
            b += 1

    return interval


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    firstList = [[0, 2], [5, 10], [13, 23], [24, 25]]
    secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]
    print(intervalIntersection(firstList, secondList)) # [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

    firstList = [[1, 3], [5, 9]]
    secondList = []
    print(intervalIntersection(firstList, secondList)) # []

    firstList = []
    secondList = [[4, 8], [10, 12]]
    print(intervalIntersection(firstList, secondList)) # []

    firstList = [[1, 7]]
    secondList = [[3, 10]]
    print(intervalIntersection(firstList, secondList)) # [[3,7]]

    firstList = [[3, 5], [9, 20]]
    secondList = [[4, 5], [7, 10], [11, 12], [14, 15], [16, 20]]
    print(intervalIntersection(firstList, secondList)) # [[4, 5], [9, 10], [11, 12], [14, 15], [16, 20]]
