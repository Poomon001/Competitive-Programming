from collections import deque
from typing import List

'''
    Link: https://leetcode.com/problems/daily-temperatures/
    Purpose: Determine the number of day that you have to wait for a warmer day. If there is no warmer day, put 0.
    parameter: List[int] temperatures - a list of temperature where indices are correspond to a day.
    return: List[int] answer - a list of day that you have to wait for aa warmer day
    Pre-Condition: 1 <= temperatures.length <= 10^5
                 : 30 <= temperatures[i] <= 100
    Post-Condition: none
'''
# The next greater algo: runtime: O(n), memory: O(n)
def dailyTemperatures_M1(temperatures: List[int]) -> List[int]:
    answer = [0] * len(temperatures)
    stack = deque() # (temperature, index)

    for i, temperature in enumerate(temperatures):
        if not stack:
            stack.append((temperature, i))
            continue

        while stack and temperature > stack[-1][0]:
            top_stack = stack.pop()
            index = top_stack[1]
            answer[index] = i - index

        stack.append((temperature, i))

    return answer

'''
    Link: https://leetcode.com/problems/daily-temperatures/
    Purpose: Determine the number of day that you have to wait for a warmer day. If there is no warmer day, put 0.
    parameter: List[int] temperatures - a list of temperature where indices are correspond to a day.
    return: List[int] answer - a list of day that you have to wait for aa warmer day
    Pre-Condition: 1 <= temperatures.length <= 10^5
                 : 30 <= temperatures[i] <= 100
    Post-Condition: none
'''
# brute force: runtime: O(n^2), memory: O(1)
def dailyTemperatures_M2(temperatures: List[int]) -> List[int]:
    answer = []
    for i in range(len(temperatures)):
        index = 0
        for j in range(i, len(temperatures)):
            # if find the next greater value, add the index to answer
            if temperatures[i] < temperatures[j]:
                answer.append(index)
                break

            index += 1

            # cannot find the next greater value, add 0
            if j == len(temperatures) - 1:
                answer.append(0)

    return answer


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n+===== Solution M1 =====+\n")
    print(dailyTemperatures_M1([73, 74, 75, 71, 69, 72, 76, 73]))  # [1,1,4,2,1,1,0,0]
    print(dailyTemperatures_M1([30, 40, 50, 60]))  # [1,1,1,0]
    print(dailyTemperatures_M1([30, 60, 90]))  # [1,1,0]
    print(dailyTemperatures_M1([30]))  # [0]

    print("\n+===== Solution M2 =====+\n")
    print(dailyTemperatures_M2([73, 74, 75, 71, 69, 72, 76, 73]))  # [1,1,4,2,1,1,0,0]
    print(dailyTemperatures_M2([30, 40, 50, 60]))  # [1,1,1,0]
    print(dailyTemperatures_M2([30, 60, 90]))  # [1,1,0]
    print(dailyTemperatures_M2([30]))  # [0]

