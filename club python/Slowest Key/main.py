from typing import List

'''
     Link: https://leetcode.com/problems/slowest-key/
     Purpose: Find the key of the keypress that had the longest duration 
     Parameter: array[int] releaseTimes - a list of time where each key is released in a sorted order
              : string keysPressed - a string of key press 
    Returns: string - the key of the keypress that had the longest duration
           : if more than one longest keypress return the one that has the highest lexicographical value 
    Pre-Condition: releaseTimes.length == n
                 : keysPressed.length == n
                 : 2 <= n <= 1000
                 : 1 <= releaseTimes[i] <= 109
                 : releaseTimes[i] < releaseTimes[i+1]
                 : keysPressed contains only lowercase English letters.
    Post-Condition: none
'''
def slowestKey(releaseTimes: List[int], keysPressed: str) -> str:
    # keep track of the longest time
    longestDuration = abs(0-releaseTimes[0])

    # keep track of slowest key (can be more than one longest key press)
    slowestKey = keysPressed[0]

    for i in range(len(releaseTimes)-1):
        duration = abs(releaseTimes[i] - releaseTimes[i+1])

        # case 1: there are 2 longest local duration
        if duration == longestDuration:
            # check if which keypress value is higher (ascii value)
            if keysPressed[i+1] > slowestKey:
                slowestKey = keysPressed[i+1]
                continue
            else:
                continue

        # case 2: the curr duration is longer than the recorded longestTime
        if duration > longestDuration:
            longestDuration = duration
            slowestKey = keysPressed[i+1]

    return slowestKey


if __name__ == '__main__':
   releaseTimes = [9,29,49,80]
   keysPressed = "cbcd"
   print(slowestKey(releaseTimes, keysPressed)) # d

   releaseTimes = [9, 29, 49, 50]
   keysPressed = "cbcd"
   print(slowestKey(releaseTimes, keysPressed)) # c

   releaseTimes = [12, 23, 36, 46, 62]
   keysPressed = "spuda"
   print(slowestKey(releaseTimes, keysPressed))  # a

   releaseTimes = [1, 2, 3, 4, 5, 6]
   keysPressed = "poooom"
   print(slowestKey(releaseTimes, keysPressed))  # p
