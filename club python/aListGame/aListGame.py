# https://open.kattis.com/problems/listgame
# Still Time Limit Exceeded

given = int(input())
count = 0
x = 0
key = True
''' loop 'given' times '''
for y in range(given):

    ''' increment divisor by 1 every loop '''
    if key == True:
        x += 1

    ''' if given number is devided by any number + 1 and results in 0 remainder '''
    if given%(x+1) == 0:

        ''' add a term that will multipy to cause 'given' by 1 term '''
        count += 1

        ''' update given number '''
        given = given//(x+1)

        ''' try the same number '''
        key = False
    else:

        ''' the same number does not work increment it by 1 '''
        key = True

    if given == 1:
        break

print(count)