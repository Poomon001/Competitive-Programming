from typing import List

'''
    Link: https://leetcode.com/problems/fizz-buzz/
    Purpose: return a string array answer
           : answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
           : answer[i] == "Fizz" if i is divisible by 3.
           : answer[i] == "Buzz" if i is divisible by 5.
           : answer[i] == i if non of the above conditions are true.r
    parameter: int n - an integer
    return: List[str]: a string array answer
    Pre-Condition: 1 <= n <= 10^4
    Post-Condition: none
'''
def fizzBuzz(n: int) -> List[str]:
    answer =[]
    for i in range(1, n+1):
        if i%3 == i%5 == 0:
            answer.append("FizzBuzz")
        elif i%3 == 0:
            answer.append("Fizz")
        elif i%5 == 0:
            answer.append("Buzz")
        else:
            answer.append(f"{i}")
    return answer


if __name__ == '__main__':
    print(fizzBuzz(3))
    print(fizzBuzz(5))
    print(fizzBuzz(15))

