'''
    Link: https://leetcode.com/problems/climbing-stairs/
    Purpose:  find how many distinct ways can you climb to the top? A staircase has n steps. Each time you can either climb 1 or 2 steps.
    parameter: int n - a number of steps a staircase has.
    return: int - a number of distinct ways can you climb to the top
    Pre-Condition: 1 <= n <= 45
    Post-Condition: none
'''
# brute force (recursive): run-time O(2^n), memory: O(n)
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
# Dynamic programming: O(n), memory: O(1)
def climbStairs_M2(n: int) -> int:
    # if you draw enough patterns on paper, you will find that n step = (n - 1) + (n - 2) steps
    stepOne = 1
    stepTwo = 1
    for i in range(1, n):
        if i % 2 == 0:
            stepOne =  stepOne + stepTwo
        else:
            stepTwo =  stepOne + stepTwo
    return stepOne if stepOne > stepTwo else stepTwo


'''
    Link: https://leetcode.com/problems/climbing-stairs/
    Purpose:  find how many distinct ways can you climb to the top? A staircase has n steps. Each time you can either climb 1 or 2 steps.
    parameter: int n - a number of steps a staircase has.
    return: int - a number of distinct ways can you climb to the top
    Pre-Condition: 1 <= n <= 45
    Post-Condition: none
'''
# dynamic programming (recursive): programming: O(n), memory: O(n)
def climbStairs_M3(n: int) -> int:
    # if we are at 3th level, down by 1 step will take to 2nd level or down by 2 steps will take to 1st level.
    # from given at 1st level has 1 and 2nd level has 2 unique steps. total unique step from 3th level = 3
    memory = {1: 1, 2: 2}

    def recursive(n: int) -> int:
        if n == 1:
            return 1

        if n == 2:
            return 2

        # memorize
        if n - 1 in memory and n - 2 in memory:
            memory[n] = memory[n - 1] + memory[n - 2]

        # recursive call
        if n not in memory:
            return recursive(n - 1) + recursive(n - 2)
        else:
            return memory[n - 1] + memory[n - 2]

    return recursive(n)

'''
    Link: https://leetcode.com/problems/climbing-stairs/
    Purpose:  find how many distinct ways can you climb to the top? A staircase has n steps. Each time you can either climb 1 or 2 steps.
    parameter: int n - a number of steps a staircase has.
    return: int - a number of distinct ways can you climb to the top
    Pre-Condition: 1 <= n <= 45
    Post-Condition: none
'''
# dynamic programming (non recursive): programming: O(n), memory: O(n)
def climbStairs_M4(n: int) -> int:
    # {number of stairs, distinct ways}
    memory = {1: 1, 2: 2}
    m = 2
    while m < n:
        m += 1
        memory[m] = memory[m - 1] + memory[m - 2]
    return memory[n]

'''
    Link: https://leetcode.com/problems/climbing-stairs/
    Purpose:  find how many distinct ways can you climb to the top? A staircase has n steps. Each time you can either climb 1 or 2 steps.
    parameter: int n - a number of steps a staircase has.
    return: int - a number of distinct ways can you climb to the top
    Pre-Condition: 1 <= n <= 45
    Post-Condition: none
'''
# dynamic programming (non recursive): programming: O(n), memory: O(1)
def climbStairs_M5(n: int) -> int:
    currMaxDistinct = 2
    prevMaxDistinct = 1

    for step in range(n):
        if n == 1:
            return prevMaxDistinct

        if n == 2:
            return currMaxDistinct

        if step > 1:
            temp = currMaxDistinct
            currMaxDistinct = prevMaxDistinct + currMaxDistinct
            prevMaxDistinct = temp

    return currMaxDistinct

# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print("\n === Solution 1 ===\n")
    print(climbStairs_M1(2)) # 2
    print(climbStairs_M1(3)) # 3
    print(climbStairs_M1(4)) # 5
    print(climbStairs_M1(5))  # 8
    print(climbStairs_M1(38)) # 63245986 - this will take a while to complete

    print("\n === Solution 2 ===\n")
    print(climbStairs_M2(2)) # 2
    print(climbStairs_M2(3)) # 3
    print(climbStairs_M2(4)) # 5
    print(climbStairs_M2(5))  # 8
    print(climbStairs_M2(38)) # 63245986

    print("\n === Solution 3 ===\n")
    print(climbStairs_M3(2))  # 2
    print(climbStairs_M3(3))  # 3
    print(climbStairs_M3(4))  # 5
    print(climbStairs_M3(5))  # 8
    print(climbStairs_M3(38))  # 63245986

    print("\n === Solution 4 ===\n")
    print(climbStairs_M4(2))  # 2
    print(climbStairs_M4(3))  # 3
    print(climbStairs_M4(4))  # 5
    print(climbStairs_M4(5))  # 8
    print(climbStairs_M4(38))  # 63245986

    print("\n === Solution 5 ===\n")
    print(climbStairs_M4(2))  # 2
    print(climbStairs_M4(3))  # 3
    print(climbStairs_M4(4))  # 5
    print(climbStairs_M4(5))  # 8
    print(climbStairs_M4(38))  # 63245986
