'''
    Link: https://leetcode.com/problems/climbing-stairs/
    Purpose:  find how many distinct ways can you climb to the top? A staircase has n steps. Each time you can either climb 1 or 2 steps.
    parameter: int n - a number of steps a staircase has.
    return: int - a number of distinct ways can you climb to the top
    Pre-Condition: 1 <= n <= 45
    Post-Condition: none
'''
# brute force: run-time O(2^n)
def climbStairs_M1(n: int) -> int:
    # count all possible cases
    if n <= 1:
        return 1
    return climbStairs_M1(n-1) + climbStairs_M1(n-2)

'''
    Link: https://leetcode.com/problems/climbing-stairs/
    Purpose:  find how many distinct ways can you climb to the top? A staircase has n steps. Each time you can either climb 1 or 2 steps.
    parameter: int n - a number of steps a staircase has.
    return: int - a number of distinct ways can you climb to the top
    Pre-Condition: 1 <= n <= 45
    Post-Condition: none
'''
# Dynamic programming: O(n)
def climbStairs_M2(n: int) -> int:
    # if you draw enough patterns on paper, you will find that n step = (n - 1) + (n - 2) steps
    stepOne = 1
    stepTwo = 1
    for i in range(1, n):
        if i % 2 == 0:
            stepOne =  stepOne + stepTwo
        else:
            stepTwo =  stepOne + stepTwo
    return  stepOne if  stepOne > stepTwo else stepTwo




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n === Solution 1 ===\n")
    print(climbStairs_M1(2)) # 2
    print(climbStairs_M1(3)) # 3
    print(climbStairs_M1(4)) # 5
    print(climbStairs_M1(38)) # 63245986 - this will take a while to complete

    print("\n === Solution 2 ===\n")
    print(climbStairs_M2(2)) # 2
    print(climbStairs_M2(3)) # 3
    print(climbStairs_M2(4)) # 5
    print(climbStairs_M2(38)) # 63245986
