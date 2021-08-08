def fibonacci(sequence):
    if(sequence == 0):
        return 0

    if (sequence <= 2):
        return 1
    return fibonacci(sequence - 1) + fibonacci(sequence - 2)

for x in range(8):
    print(fibonacci(x), '-->', x)
