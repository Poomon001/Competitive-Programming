from typing import List, Tuple
from bisect import bisect


# p(j) = i:
# j = index of job j
# i = index of any previous job that is compatible with job j
# O(n^2) - linear search
def prevCompatibleJobs(jobs: List[Tuple[int, int, int]]) -> List[int]:
    p = [-1] * len(jobs)

    for j in range(len(jobs) - 1, -1, -1):
        for i in range(j - 1, -1, -1):
            # compatible if currStart is after prevEnd
            if jobs[j][0] >= jobs[i][1]:
                p[j] = i
                break
    return p

# p(j) = i:
# j = index of job j
# i = index of any previous job that is compatible with job j
# O(nlogn) - binary search
def improvedPrevCompatibleJobs(jobs: List[Tuple[int, int, int]]) -> List[int]:
    p = [-1] * len(jobs)
    start = [job[0] for job in jobs]
    finish = [job[1] for job in jobs]

    for j in range(len(jobs)):
        # start searches for the nearest finish. Return the nearest finish index.
        i = bisect(finish, start[j]) - 1
        p[j] = i

    return p

'''
    Link: https://leetcode.com/problems/maximum-profit-in-job-scheduling/
    Purpose: Find the subset of compatible jobs with the maximum weight
           : Two jobs are compatible if they don’t overlap
           : Job i and j are compatible if and only if fj is less than si OR fi is less than sj
    parameter: List[int] startTime- a list of start time of job i where i is the index
             : List[int] finishTime- a list of finish time of job i where i is the index
             : List[int] profit- a list of weight of job i where i is the index
    return: List[Tuple[int, int, int]] - a subset compatible jobs [start, finish, weight] that produce the maximum profit
    Pre-Condition: 1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
                 : 1 <= startTime[i] < endTime[i] <= 10^9
                 : 1 <= profit[i] <= 10^4
    Post-Condition: none
'''
# runtime - O(nlogn), memory - O(n)
def jobScheduling(startTime: List[int], endTime: List[int], profit: List[int]) -> List[Tuple[int, int, int]]:
    jobs = sorted(zip(startTime, endTime, profit), key=lambda a: a[1])
    list = []

    # cache(j) = i
    # j = job's index
    # i = optimal profit at job j
    cache = [None] * len(jobs)

    p = improvedPrevCompatibleJobs(jobs)

    def findOpt(j):
        # base case
        if j == -1:
            return 0

        if cache[j] != None:
            return cache[j]

        # select 1. not the current job or 2. current job
        # 1. look for a job before the current job
        # 2. pick the current job and move to the previous job that doesn't conflict with the current job
        optProfit = max(findOpt(j - 1), jobs[j][2] + findOpt(p[j]))
        cache[j] = optProfit

        return optProfit

    def getList(j):
        # base case
        if j == -1:
            return

        if jobs[j][2] + findOpt(p[j]) >= findOpt(j - 1):
            list.append(jobs[j])
            getList(p[j])
        else:
            getList(j - 1)

    getList(len(jobs) - 1)

    return list

'''
    Link: https://leetcode.com/problems/maximum-profit-in-job-scheduling/
    Purpose: Find the maximum profit of non-conflict (compatible) jobs in a jobs list
           : Two jobs are compatible if they don’t overlap
           : Job i and j are compatible if and only if fj is less than si OR fi is less than sj 
    parameter: List[int] startTime- a list of start time of job i where i is the index
             : List[int] finishTime- a list of finish time of job i where i is the index
             : List[int] profit- a list of weight of job i where i is the index
    return: int -  the maximum profit of non-conflict jobs in a jobs list
    Pre-Condition: 1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
                 : 1 <= startTime[i] < endTime[i] <= 10^9
                 : 1 <= profit[i] <= 10^4
    Post-Condition: none
'''
# Backtrack recursive: runtime - O(2^n), memory - O(n)
def jobScheduling_M1(startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    jobs = sorted(zip(startTime, endTime, profit), key=lambda a: a[1])

    p = improvedPrevCompatibleJobs(jobs)

    def findOpt(j):
        # base case
        if j == -1:
            return 0

        optProfit = max(findOpt(j - 1), jobs[j][2] + findOpt(p[j]))

        return optProfit

    return findOpt(len(jobs) - 1)

'''
    Link: https://leetcode.com/problems/maximum-profit-in-job-scheduling/
    Purpose: Find the maximum profit of non-conflict (compatible) jobs in a jobs list
           : Two jobs are compatible if they don’t overlap
           : Job i and j are compatible if and only if fj is less than si OR fi is less than sj 
    parameter: List[int] startTime- a list of start time of job i where i is the index
             : List[int] finishTime- a list of finish time of job i where i is the index
             : List[int] profit- a list of weight of job i where i is the index
    return: int -  the maximum profit of non-conflict jobs in a jobs list
    Pre-Condition: 1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
                 : 1 <= startTime[i] < endTime[i] <= 10^9
                 : 1 <= profit[i] <= 10^4
    Post-Condition: none
'''
# Dynamic programming - linear search: runtime - O(n^2), memory - O(n)
def jobScheduling_M2(startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    jobs = sorted(zip(startTime, endTime, profit), key=lambda a: a[1])

    # cache(j) = i
    # j = job's index
    # i = optimal profit at job j
    cache = [None] * len(jobs)

    p = prevCompatibleJobs(jobs)

    def findOpt(j):
        # base case
        if j == -1:
            return 0

        if cache[j] != None:
            return cache[j]

        # select 1. not the current job or 2. current job
        # 1. look for a job before the current job
        # 2. pick the current job and move to the previous job that doesn't conflict with the current job
        optProfit = max(findOpt(j - 1), jobs[j][2] + findOpt(p[j]))
        cache[j] = optProfit

        return optProfit

    return findOpt(len(jobs) - 1)

'''
    Link: https://leetcode.com/problems/maximum-profit-in-job-scheduling/
    Purpose: Find the maximum profit of non-conflict (compatible) jobs in a jobs list
           : Two jobs are compatible if they don’t overlap
           : Job i and j are compatible if and only if fj is less than si OR fi is less than sj 
    parameter: List[int] startTime- a list of start time of job i where i is the index
             : List[int] finishTime- a list of finish time of job i where i is the index
             : List[int] profit- a list of weight of job i where i is the index
    return: int -  the maximum profit of non-conflict jobs in a jobs list
    Pre-Condition: 1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4
                 : 1 <= startTime[i] < endTime[i] <= 10^9
                 : 1 <= profit[i] <= 10^4
    Post-Condition: none
'''
# Dynamic programming - binary search: runtime - O(nlogn), memory - O(n)
def jobScheduling_M3(startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    jobs = sorted(zip(startTime, endTime, profit), key=lambda a: a[1])

    # cache(j) = i
    # j = job's index
    # i = optimal profit at job j
    cache = [None] * len(jobs)

    p = improvedPrevCompatibleJobs(jobs)

    def findOpt(j):
        # base case
        if j == -1:
            return 0

        if cache[j] != None:
            return cache[j]

        # select 1. not the current job or 2. current job
        # 1. look for a job before the current job
        # 2. pick the current job and move to the previous job that doesn't conflict with the current job
        optProfit = max(findOpt(j - 1), jobs[j][2] + findOpt(p[j]))
        cache[j] = optProfit

        return optProfit

    return findOpt(len(jobs) - 1)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n === Solution 1 === \n")
    print(jobScheduling_M1([1,2,3,3], [3,4,5,6], [50,10,40,70])) # 120
    print(jobScheduling_M1([1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60])) # 150
    print(jobScheduling_M1([1,1,1], [2,3,4], [5,6,4])) # 6
    print(jobScheduling_M1([0, 1, 3, 3, 4, 5, 6, 8], [6, 4, 5, 8, 7, 9, 10, 11], [6, 3, 2, 5, 3, 4, 4, 3])) # 10

    print("\n === Solution 2 === \n")
    print(jobScheduling_M2([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]))  # 120
    print(jobScheduling_M2([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60]))  # 150
    print(jobScheduling_M2([1, 1, 1], [2, 3, 4], [5, 6, 4]))  # 6
    print(jobScheduling_M2([0, 1, 3, 3, 4, 5, 6, 8], [6, 4, 5, 8, 7, 9, 10, 11], [6, 3, 2, 5, 3, 4, 4, 3]))  # 10

    print("\n === Solution 3 === \n")
    print(jobScheduling_M3([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]))  # 120
    print(jobScheduling_M3([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60]))  # 150
    print(jobScheduling_M3([1, 1, 1], [2, 3, 4], [5, 6, 4]))  # 6
    print(jobScheduling_M3([0, 1, 3, 3, 4, 5, 6, 8], [6, 4, 5, 8, 7, 9, 10, 11], [6, 3, 2, 5, 3, 4, 4, 3]))  # 10

    print("\n === Subset Solution === \n")
    print(jobScheduling([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70]))  # [(3, 6, 70), (1, 3, 50)]
    print(jobScheduling([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60]))  # [(6, 9, 60), (4, 6, 70), (1, 3, 20)]
    print(jobScheduling([1, 1, 1], [2, 3, 4], [5, 6, 4]))  # [(1, 3, 6)]
    print(jobScheduling([0, 1, 3, 3, 4, 5, 6, 8], [6, 4, 5, 8, 7, 9, 10, 11], [6, 3, 2, 5, 3, 4, 4, 3]))  # [(6, 10, 4), (0, 6, 6)]

