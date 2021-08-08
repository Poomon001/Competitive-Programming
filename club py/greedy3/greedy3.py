'''
    Purpose: putpose to print string that doesnt contain any a duplicate character and finish when found a duplicate
    Input: array - contains characters
    Print: string - string that contains non duplicate characters
    Pre-Condition: input not empty
                 : input must be in either upper or lower case
    Post-Condition: none
'''
input = "ABCDEDCBA"
str = ""

#loop through input char
for x in range(0, len(input)):

    #case 1: input contains only one char, print it ans finish program
    if(len(input) == 1):
        print(input)
        break
    #case 2: contain two or more char
    #if a target char is in a str, print the result and finish loop
    if((input[x] in str)):
        print(str)
        break

    #store a current char in str
    str += input[x]
