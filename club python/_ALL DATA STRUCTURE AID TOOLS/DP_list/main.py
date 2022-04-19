import time
start_time = time.time()

def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num-1)

# def factorial(num):
#     result = num
#     for x in range(num):
#         if x != 0:
#             result *= x
#     return result

print(factorial(10))

print("--- %s seconds ---" % (time.time() - start_time))