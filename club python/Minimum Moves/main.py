from collections import Counter

'''
    Purpose: Given a sorted integer array. Find the minimum moves to make every x value in the array occur exactly x times.
           : adding or removing a number x is consider as 1 move.
           : eg - [1, 2, 2, 4] -> removing 4 once is 1 move [1, 2, 2] works
                               -> adding 3 4s is 3 moves [1, 2, 2, 4, 4, 4, 4] works    
    parameter: List[int] nums - a list of sorted integers
    return: int - a minimum moves to make every x value in the array occur exactly x times.
    Pre-Condition: 1 <= nums.length <= 5 * 10^5
                 : 1 <= nums[i] <= 2^31 - 1
    Post-Condition: none
'''
# time: O(n), space: O(m) where m is set(A)
def minimumMoves(A):
    # {num : counter}
    dic = Counter(A)
    ans = 0

    for num, count in dic.items():
        # get a number of adds that needs
        add = abs(num - count)

        # compare the number of adds with number of removes (current counter = a number of needed removes)
        ans += min(add, count)

    return ans


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(minimumMoves([1,1,3,4,4,4])) # 3
    print(minimumMoves([1, 2, 2, 2, 5, 5, 5, 8])) # 4
    print(minimumMoves([1,1,1,1,3,3,4,4,4,4,4])) # 5
    print(minimumMoves([10,10,10])) # 3
    print(minimumMoves([2])) # 1
    print(minimumMoves([1]))  # 0

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
