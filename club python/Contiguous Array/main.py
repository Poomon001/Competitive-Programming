from typing import List
'''
    Link: https://leetcode.com/problems/contiguous-array/
    Purpose: Find the maximum length of a contiguous subarray with an equal number of 0 and 1.
           : Means a connection of 1 and 0 where 1 and 0 must be equal. eg (0,0,0,1,1,1) = 6,  (0,0,0,0,1,0,1,0) = 4,  (1,0,0,0,0,1,0,1,0) = 4
    parameter: List[int] nums - a list of binary numbers
    return: int ans - the maximum length
    Pre-Condition: 1 <= nums.length <= 10^5
                 : nums[i] is either 0 or 1.
    Post-Condition: none
'''

'''
Keep track of the local max length by:
   :+1 when meeting 1
   :-1 when meeting 0
   :when count == 0, we get the first max length by subtract(curr index, starting index)
   :when count == ans.keys, we get new length by subtract(curr index, previous ans index)
'''

def findMaxLength(nums: List[int]) -> int:
    '''
        Keep track of the local max length by:
           :+1 when meeting 1
           :-1 when meeting 0
           :when count == ans.keys, we get new length by subtract(curr index, previous matching index)
        '''

def findMaxLength(nums: List[int]) -> int:
    # sum is 0 at at index of -1 {count, index}
    ans = {0: -1}
    maxLength = 0
    count = 0

    for index, val in enumerate(nums):
        if val == 0:
            count -= 1
        else:
            count += 1

        # check the rest contiguous subarray
        if count in ans:
            length = index - ans[count]  # curr index - matching index
            # print(length, index, ans[count])
            maxLength = max(maxLength, length)
        else:
            ans[count] = index

    return maxLength


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(findMaxLength([0])) # 0
    print(findMaxLength([0,1])) # 2
    print(findMaxLength([1, 0])) # 2
    print(findMaxLength([0, 1, 0])) # 2
    print(findMaxLength([0,0,0,1,0,1,1,1,0])) # 8
    print(findMaxLength([0,0,0,1,1,1,0])) # 6
    print(findMaxLength([0,0,0,1,1,1,0,0,0,0])) # 6
    print(findMaxLength([0,0,0,1,1,1])) # 6
    print(findMaxLength([0,0,0,1,1,1,0,0,0,0,0,0,0,1,1,1,0,0,0,1,1,1])) # 12

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
