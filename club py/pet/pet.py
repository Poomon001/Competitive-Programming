'''
    Link: https://open.kattis.com/problems/pet
    Purpose: Write a program that determines the winner and how many points they got.
    Input: int - Five lines, each containing 4 integers
    Print: string - a single line the winner’s number and their points
    Pre-Condition : non empty input
    Post-Condition: none
'''

maxIndex = 0
max = 0
for x in range(5):
    sumGrade = 0
    grade1, grade2, grade3, grade4 = list(map(int, input().split()))
    sumGrade = grade1 + grade2 + grade3 + grade4
    if(sumGrade > max):
        max = sumGrade
        maxIndex = x
print(maxIndex+1, max)

