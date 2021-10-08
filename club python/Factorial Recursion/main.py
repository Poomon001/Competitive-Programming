# Recursive
def factorial_M1(num):
    if num <= 1:
        return 1
    return num * factorial_M1(num-1)

# loop
def factorial_M2(num):
    result = num
    for x in range(num):
        if x != 0:
            result *= x
    return result

print(factorial_M1(10))

print(factorial_M2(10))

