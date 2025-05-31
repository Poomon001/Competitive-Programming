'''
    Link: https://leetcode.com/problems/subsets-ii/
    Purpose: Find all subsets, excluding duplicate subset.
    parameter: List[int] nums - a list of numbers
    return: List[List[int]] - all subsets in nums, excluding duplicate subset.
    Pre-Condition: 1 <= nums.length <= 10
                 : -10 <= nums[i] <= 10
    Post-Condition: none
'''
# iterative - runtime: O(n*2^n), memory: O(n*2^n) -> we have 2^n subsets each many contain n elements
def subsetsWithDup(nums):
    nums.sort()
    subsets = [[]]
    end = 0
    '''
    1, 2, 2, 2
    []
    [] [1]
    [] [1] [2] [1, 2]
    [] [1] [2] [1, 2] | [2, 2] [1, 2, 2]
    [] [1] [2] [1, 2] [2, 2] [1, 2, 2] | [2, 2, 2] [1, 2, 2, 2] 
    '''
    # observe from pattern:
    # if a  duplicate processes, consider processing from only previous subsets added
    for i in range(len(nums)):
        # use prev end index to process from only previous uebsets added
        start = end if i >= 1 and nums[i] == nums[i - 1] else 0
        end = len(subsets)
        for j in range(start, end):
            subset = subsets[j][:]
            subset.append(nums[i])
            subsets.append(subset)

    return subsets


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(subsetsWithDup([1, 2, 2])) # [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]
    print(subsetsWithDup([1, 2, 2, 2])) # [[], [1], [2], [1, 2], [2, 2], [1, 2, 2], [2, 2, 2], [1, 2, 2, 2]]
    print(subsetsWithDup([2, 1, 2])) # [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]
    print(subsetsWithDup([0])) # [[], [0]]
    print(subsetsWithDup([1, 1])) # [[], [1], [1, 1]]
    print(subsetsWithDup([1, 1, 1])) # [[], [1], [1, 1], [1, 1, 1]]

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
