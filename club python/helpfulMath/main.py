'''
    Link: https://codeforces.com/contest/339/problem/A
    Purpose: Rearrange the summans and print the sum in such a way that Xenia can calculate the sum.
    Input: sting - a list of numbers separate with "+"
    Print: string - an arrange string
    Pre-Condition : string is not empty
    Post-Condition: none
'''

input = input()
length = int(len(input) - int(len(input) / 2))
num = input.split("+")
first = 0
num = sorted(num)

for i in range(length):
    if (i == length - 1):
        print(num[i], "", end="", sep="")
    else:
        print(num[i], "+", end="", sep="")