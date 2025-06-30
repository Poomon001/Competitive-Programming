from typing import List

'''     
    Link: https://leetcode.com/problems/merge-intervals
    Purpose: Merge all overlapping intervals from a given array of intervals where intervals[i] = [start, end]
    Parameter: List[List[int]] intervals - a list of intervals
    Returns: List[List[int]] ans - a list of merged intervals
    Pre-Condition: 1 <= intervals.length <= 10^4
                 : intervals[i].length == 2
                 : 0 <= start <= end <= 10^4
    Post-Condition: none
'''
# run-time: O(n), memory: O(n)
def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals = sorted(intervals, key=lambda x: x[0])
    ans = [intervals[0]]
    for interval in intervals:
        head = ans[-1]  # the last element in answer list

        # update end only
        if head[0] <= interval[0] <= head[1]:
            update = [head[0], max(interval[1], head[1])]
            ans.pop()
            ans.append(update)

        # start a new interval
        elif head[1] < interval[0]:
            ans.append(interval)

    return ans


if __name__ == '__main__':
    print(merge([[1, 3], [8, 10], [15, 18], [2, 6]])) # [[1, 6], [8, 10], [15, 18]]
    print(merge([[1,3], [2,6], [8,10], [15,18]])) # [[1, 6], [8, 10], [15, 18]]
    print(merge([[1, 3], [8, 10], [3, 18], [2, 6]])) # [[1, 18]]
    print(merge([[1,4], [4,5]])) # [[1, 5]]
    print(merge([[1,4], [0,4]])) # [[0, 4]]
    print(merge([[1,4], [2,3]])) # [[1, 4]]
    print(merge([[1, 10]])) # [[1, 10]]
