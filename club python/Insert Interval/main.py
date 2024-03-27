from typing import List

'''
    Link: https://leetcode.com/problems/insert-interval
    Purpose: Given array of list intervals [start, end], and a new interval
           : Find a new array of list interval after inserting the new interval
    parameter: List[List[int]] intervals - a list of list intervals
    return: List[int] newInterval - a new interval
    Pre-Condition: 0 <= intervals.length <= 10^4
                 : intervals[i].length == 2
                 : 0 <= start <= end <= 10^5
                 : intervals is sorted by start in ascending order.
                 : newInterval.length == 2
                 : 0 <= start <= end <= 10^5
    Post-Condition: None
'''
# brute force - run time: O(n), memory: O(1)
def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    ans = []
    newStart = newInterval[0]
    newEnd = newInterval[1]

    for interval in intervals:
        start = interval[0]
        end = interval[1]

        if newEnd < start:
            ans.append([newStart, newEnd])
            ans.extend(intervals[intervals.index(interval):])
            return ans

        # check if there is an overlap
        # yes, create a new interval to cover the entire overlap
        # no, append curr interval
        if newStart <= end and newEnd >= start:
            newStart = min(newStart, start)
            newEnd = max(newEnd, end)
        else:
            ans.append(interval)

    # if there is intersection til the end of the intervals list
    ans.append([newStart, newEnd])
    return ans

if __name__ == "__main__":
    print(insert([[1,3],[6,9]], [2,5])) # [[1, 5], [6, 9]]
    print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4, 8])) # [[1, 2], [3, 10], [12, 16]]
    print(insert([[3, 5], [6, 7], [8, 10], [12, 16]], [1, 2])) # [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [17, 20])) # [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16], [17, 20]]
    print(insert([[1, 2], [3, 5], [8, 10], [12, 16]], [6, 7])) # [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    print(insert([[1, 2], [3, 5], [8, 10], [12, 16]], [3, 6])) # [[1, 2], [3, 6], [8, 10], [12, 16]]
    print(insert([], [5, 7]))  # [[5, 7]]
    print(insert([[1, 5]], [2, 3]))  # [[1,5]]
    print(insert([[1,3],[6,9]], [2, 5]))  # [[1, 5], [6, 9]]

