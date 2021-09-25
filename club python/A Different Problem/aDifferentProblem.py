'''
     * Link: https://open.kattis.com/submissions/7501121
     * Purpose: Write a program that computes the difference between non-negative integers.
     * Parameters: none
     * Returns: none
     * Pre-Condition: always have 2 int values per a line
     * Post-Condition: runtime 0(n) and terminate the loop by the end of file
'''
while(True):
    # get input
    try:
        num1, num2 = map(int, input().split())
    except Exception:
        break

    if num1 > num2:
        print(num1 - num2)
    else:
        print(num2 - num1)