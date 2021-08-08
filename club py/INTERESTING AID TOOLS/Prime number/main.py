import math
ls = []
def primeCheck(given):
    result = ""
    if given > 1:
        ''' noon 2 even number is not a prime number '''
        if given % 2 == 0:
            print("it is not a prime number")
            return

        ''' to reduce the time using mathematic equation,
         you will know that we only need to check from 2 to sqrt(given number) '''
        max_divisor = math.floor(math.sqrt(given))
        for x in range(2, max_divisor + 1):

            ''' if the given number is devisible by any number between 2 and itself-1, it is not a prime '''
            if given % x == 0:
                result = "it is not a prime number because it is devicible by " + str(x)
                break
            else:
                result = "it is a prime number"
        print(result)

def listAllPrime(given):
    for x in range(2, given + 1):
        prime = True
        for y in range(2, x):
            if x % y == 0:
                prime = False
                break

        if prime:
            ls.append(x)

primeCheck(1113)
listAllPrime(2)
print(ls)