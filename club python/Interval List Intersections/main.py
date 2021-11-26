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
def intervalIntersection_M1(firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
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
def intervalIntersection_M2(firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
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

        # check for an intersection
        if front1 <= back2 and front2 <= back1:
            front = max(front1, front2)
            back = min(back1, back2)
            interval.append([front, back])

        # logically move to the next interval
        if back1 < back2:
            a += 1
        else:
            b += 1


    return interval


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    firstList1 = [[0, 2], [5, 10], [13, 23], [24, 25]]
    secondList1 = [[1, 5], [8, 12], [15, 24], [25, 26]]

    firstList2 = [[1, 3], [5, 9]]
    secondList2 = []

    firstList3 = []
    secondList3 = [[4, 8], [10, 12]]

    firstList4 = [[1, 7]]
    secondList4 = [[3, 10]]


    firstList5 = [[3, 5], [9, 20]]
    secondList5 = [[4, 5], [7, 10], [11, 12], [14, 15], [16, 20]]


    print("\n+==== M1 Solution ====+\n")
    print(intervalIntersection_M1(firstList1, secondList1))  # [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
    print(intervalIntersection_M1(firstList2, secondList2))  # []
    print(intervalIntersection_M1(firstList3, secondList3))  # []
    print(intervalIntersection_M1(firstList4, secondList4))  # [[3,7]]
    print(intervalIntersection_M1(firstList5, secondList5)) # [[4, 5], [9, 10], [11, 12], [14, 15], [16, 20]]

    print("\n+==== M2 Solution ====+\n")
    print(intervalIntersection_M2(firstList1, secondList1))  # [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
    print(intervalIntersection_M2(firstList2, secondList2))  # []
    print(intervalIntersection_M2(firstList3, secondList3))  # []
    print(intervalIntersection_M2(firstList4, secondList4))  # [[3,7]]
    print(intervalIntersection_M2(firstList5, secondList5))  # [[4, 5], [9, 10], [11, 12], [14, 15], [16, 20]]
