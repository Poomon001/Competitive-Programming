'''
    Link: https://leetcode.com/problems/maximum-length-of-pair-chain/description/
    Purpose: Find the maximum subset of jobs in pairs list that is not overlapped with others
           : pair = [s, f] where s = start time and f = finish time
           : Note: all jobs worth equivalently regardless of the length
    parameter: List[List[int]] - pairs
    return: int - the number of job in the subset
    Pre-Condition: n == pairs.length
                 : 1 <= n <= 1000
                 : -1000 <= lefti < righti <= 1000
    Post-Condition: none
'''
# runtime - O(nlogn), memory - O(1)
def findLongestChain(pairs):
    # greedy - earliest finish time
    pairs.sort(key=lambda k: k[1])
    localFinish = -1001
    jobCount = 0
    for pair in pairs:
        # check compatible (overlaps)
        if (localFinish < pair[0]):
            jobCount += 1
            localFinish = pair[1]
            # print(pair)
    return jobCount


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(findLongestChain([[1, 2]])) # 1
    print(findLongestChain([[1,2],[2,3],[3,4]]))  # 2
    print(findLongestChain([[1,2],[7,8],[4,5]]))  # 3
    print(findLongestChain([[1,3],[2,3],[3,4]])) # 1
    print(findLongestChain([[0,6],[0,3],[0,18],[5,10],[8,11],[11,14],[12,18],[19,23],[20,22]])) # 4
