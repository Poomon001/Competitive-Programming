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
def subsetsWithDup_M1(nums):
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
    nums.sort()
    subsets = [[]]
    end = 0
    for i in range(len(nums)):
        # use prev end index to process from only previous uebsets added
        start = end if i >= 1 and nums[i] == nums[i - 1] else 0
        end = len(subsets)
        for j in range(start, end):
            subset = subsets[j][:]
            subset.append(nums[i])
            subsets.append(subset)

    return subsets

'''
    Link: https://leetcode.com/problems/subsets-ii/
    Purpose: Find all subsets, excluding duplicate subset.
    parameter: List[int] nums - a list of numbers
    return: List[List[int]] - all subsets in nums, excluding duplicate subset.
    Pre-Condition: 1 <= nums.length <= 10
                 : -10 <= nums[i] <= 10
    Post-Condition: none
'''
# recursively - runtime: O(n*2^n), memory: O(n*2^n) -> we have 2^n subsets each many contain n elements
def subsetsWithDup_M2(nums):
    '''
                           []
                /          |          \
              [1]         [2]         [2]
            /     \      /   \         |
        [1,2]   [1,2]  [2,2]  ×       ×
         /         |     |
     [1,2,3]       ×     ×
    '''
    subsets = []
    nums.sort()

    def backtrack(i, subset):
        subsets.append(subset[:])
        for j in range(i, len(nums)):
            # Skip duplicates at the same level
            if j > i and nums[j] == nums[j - 1]:
                continue
            subset.append(nums[j])
            backtrack(j + 1, subset)
            subset.pop()

    backtrack(0, [])
    return subsets


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n === Solution 1 === \n")
    print(subsetsWithDup_M1([1, 2, 2])) # [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]
    print(subsetsWithDup_M1([1, 2, 2, 2])) # [[], [1], [2], [1, 2], [2, 2], [1, 2, 2], [2, 2, 2], [1, 2, 2, 2]]
    print(subsetsWithDup_M1([2, 1, 2])) # [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]
    print(subsetsWithDup_M1([0])) # [[], [0]]
    print(subsetsWithDup_M1([1, 1])) # [[], [1], [1, 1]]
    print(subsetsWithDup_M1([1, 1, 1])) # [[], [1], [1, 1], [1, 1, 1]]

    print("\n === Solution 2 === \n")
    print(subsetsWithDup_M2([1, 2, 2]))  # [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]
    print(subsetsWithDup_M2([1, 2, 2, 2]))  # [[], [1], [2], [1, 2], [2, 2], [1, 2, 2], [2, 2, 2], [1, 2, 2, 2]]
    print(subsetsWithDup_M2([2, 1, 2]))  # [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]
    print(subsetsWithDup_M2([0]))  # [[], [0]]
    print(subsetsWithDup_M2([1, 1]))  # [[], [1], [1, 1]]
    print(subsetsWithDup_M2([1, 1, 1]))  # [[], [1], [1, 1], [1, 1, 1]]

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
