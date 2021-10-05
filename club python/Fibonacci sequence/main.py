# run-time O(2^n)
def fibonacci_M1(sequence):
    if(sequence == 0):
        return 0

    if (sequence <= 2):
        return 1
    return fibonacci_M1(sequence - 1) + fibonacci_M1(sequence - 2)

# runtime O(n)
def fibonacci_M2(sequence):
    sum = [0, 1]
    for i in range(sequence):
        sum.append(sum[i] + sum[i+1])

    return sum[sequence]

for x in range(8):
    print(fibonacci_M1(x), '-->', x)

print("\n=== Complete M1 ===\n")

for x in range(8):
    print(fibonacci_M2(x), '-->', x)
