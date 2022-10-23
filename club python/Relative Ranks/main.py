from typing import List

'''
    Link: https://leetcode.com/problems/relative-ranks/
    Purpose: Determine the placement of the scores.
    parameter: List[Int] scores - a list of unique integer
    return: List[Int] rank - all ranks of the scores (rank[i] represent a rank of scores[i])
    Pre-Condition: n == score.length
                 : 1 <= n <= 104
                 : 0 <= score[i] <= 106
                 : All the values in score are unique.
    Post-Condition: none
'''
# runtime: O(nlog(n)), memory: O(n)
def findRelativeRanks(scores: List[int]) -> List[str]:
    ''' scores = [10,3,8,9,4] '''
    # {score, originalIndex}
    # to access original indices
    scoreMap = {}
    rank = [0 for i in scores]  # [0,0,0,0,0]

    for i in range(len(scores)):
        scoreMap[scores[i]] = i  # {10:0, 3:1 ,8:2 ,9:3, 4:4}

    scores.sort(reverse=True)  # 10,9,8,4,3

    for i in range(len(scores)):
        score = scores[i]
        originalIndex = scoreMap[score]
        if i == 0:
            rank[originalIndex] = "Gold Medal"
        elif i == 1:
            rank[originalIndex] = "Silver Medal"
        elif i == 2:
            rank[originalIndex] = "Bronze Medal"
        else:
            rank[originalIndex] = str(i + 1)
    return rank


if __name__ == "__main__":
    print(findRelativeRanks([5,4,3,2,1])) # ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5']
    print(findRelativeRanks([12,23,13,4,5])) # ['Bronze Medal', 'Gold Medal', 'Silver Medal', '5', '4']
    print(findRelativeRanks([20, 11, 30])) # ['Silver Medal', 'Bronze Medal', 'Gold Medal']
    print(findRelativeRanks([2,1])) # ['Gold Medal', 'Silver Medal']
    print(findRelativeRanks([20])) # ['Gold Medal']
