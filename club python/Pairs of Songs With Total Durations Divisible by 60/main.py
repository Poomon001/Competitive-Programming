from typing import List

'''
    Link: https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
    Purpose: Find the number of pairs of songs for which their total duration in seconds is divisible by 60
    parameter: List[int] time - a list of songs where the ith song has a duration of time[i] seconds.
    return: int count - the number of pairs of songs for which their total duration in seconds is divisible by 60
    Pre-Condition: 1 <= time.length <= 6 * 10^4
                 : 1 <= time[i] <= 500
    Post-Condition: none
'''
def numPairsDivisibleBy60_M1(time: List[int]) -> int:
    count = 0
    for i in range(len(time)):
        for j in range(i + 1, len(time)):
            if (time[i] + time[j]) % 60 == 0:
                count += 1

    return count

'''
    Link: https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
    Purpose: Find the number of pairs of songs for which their total duration in seconds is divisible by 60
    parameter: List[int] time - a list of songs where the ith song has a duration of time[i] seconds.
    return: int count - the number of pairs of songs for which their total duration in seconds is divisible by 60
    Pre-Condition: 1 <= time.length <= 6 * 10^4
                 : 1 <= time[i] <= 500
    Post-Condition: none
'''
def numPairsDivisibleBy60_M2(time: List[int]) -> int:
    # {remainder:total}
    remainder = {}
    count = 0

    for t in time:
        # find a remider pair from 0 to 59
        remainderPair = (60 - (t % 60)) % 60

        # add total remainder to counter
        if remainderPair in remainder:
            count += remainder[remainderPair]

        # increment total remainder
        if t % 60 in remainder:
            remainder[t % 60] += 1
        else:
            remainder[t % 60] = 1

    return count


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("\n+===== solution M1 =====+\n")
    print(numPairsDivisibleBy60_M1([30,20,150,100,40])) # 3
    print(numPairsDivisibleBy60_M1([60,60,60])) # 3
    print(numPairsDivisibleBy60_M1([30,30])) # 1
    print(numPairsDivisibleBy60_M1([50,222,276,265,137,319,471,15,158,280,9,481,372,484,254,279,256,67,178,91,497,272,149,50,400,450,128,37,33,417])) # 2
    print(numPairsDivisibleBy60_M1([158,280,9,481,372,484,254,279,256,67])) # 0

    print("\n+===== solution M2 =====+\n")
    print(numPairsDivisibleBy60_M2([30, 20, 150, 100, 40])) # 3
    print(numPairsDivisibleBy60_M2([60, 60, 60])) # 3
    print(numPairsDivisibleBy60_M2([30, 30])) # 1
    print(numPairsDivisibleBy60_M2(
        [50, 222, 276, 265, 137, 319, 471, 15, 158, 280, 9, 481, 372, 484, 254, 279, 256, 67, 178, 91, 497, 272, 149,
         50, 400, 450, 128, 37, 33, 417])) # 2
    print(numPairsDivisibleBy60_M2([158, 280, 9, 481, 372, 484, 254, 279, 256, 67])) # 0
