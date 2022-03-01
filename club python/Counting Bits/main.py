from typing import List

'''
    Link: https://leetcode.com/problems/counting-bits/
    Purpose: Find each sum of "1" in each binary representation of 0 to num.
    parameter: int n - an integer
    return: List[int] ans - a list of sum of "1" in each binary where:
          : ans[0] = sum(of "1" in each binary representation of 0), 
          : ans[1] = sum(of "1" in each binary representation of 1), ...
          : ans[num] = sum(of "1" in each binary representation of num)
    Pre-Condition: 0 <= n <= 10^5
    Post-Condition: none
'''
# runtime: O(nlog(n)), memory: O(n)
def countBits(n: int) -> List[int]:
    ans = []
    for i in range(0, n + 1):
        i = bin(i)[2:]
        ans.append(i.count("1")) # 32 bits -> log(n)

    return ans


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    '''
    0 --> 0
    1 --> 1
    2 --> 10
    3 --> 11
    4 --> 100
    5 --> 101
    '''
    print(countBits(0)) # [0]
    print(countBits(1)) # [0, 1]
    print(countBits(2)) # [0,1,1]
    print(countBits(3)) # [0,1,1,2]
    print(countBits(4)) # [0,1,1,2,1]
    print(countBits(5)) # [0,1,1,2,1,2]
