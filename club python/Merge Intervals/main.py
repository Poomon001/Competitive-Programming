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
    intervals.sort()
    answer = [intervals[0]]

    for interval in intervals:
        start = interval[0]
        end = interval[1]

        prev_interval = answer[-1]

        if prev_interval[0] <= start <= prev_interval[1]:
            # if they are in the same interval, merge
            answer[-1] = [min(start, prev_interval[0]), max(end, prev_interval[-1])]
        else:
            answer.append(interval)
    return answer


if __name__ == '__main__':
    print(merge([[1, 3], [8, 10], [15, 18], [2, 6]])) # [[1, 6], [8, 10], [15, 18]]
    print(merge([[1,3], [2,6], [8,10], [15,18]])) # [[1, 6], [8, 10], [15, 18]]
    print(merge([[1, 3], [8, 10], [3, 18], [2, 6]])) # [[1, 18]]
    print(merge([[1,4], [4,5]])) # [[1, 5]]
    print(merge([[1,4], [0,4]])) # [[0, 4]]
    print(merge([[1,4], [2,3]])) # [[1, 4]]
    print(merge([[1, 10]])) # [[1, 10]]
