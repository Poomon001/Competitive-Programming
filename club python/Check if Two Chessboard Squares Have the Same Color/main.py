# Online Python compiler (interpreter) to run Python online.
def print_all_codes(n, m):

    upper_bound = m + n

    # Print all codes for n and m

    def print_01_codes(current, num_digits):

        if num_digits == 0:

            # Print only the current

            print(current)

        else:

            if upper_bound > m or upper_bound < 1 or m == n == 0:

                print_01_codes('1' + current, num_digits - 1)

                print_01_codes('0' + current, num_digits - 1)

                print_01_codes('1' + current, num_digits - 1)

                print_01_codes('0' + current, num_digits - 1)

            else:

                print_01_codes('1' + current, num_digits - 1)

                print_01_codes('0' + current, num_digits - 1)

                print_01_codes('1' + current, num_digits - 1)

    upper_bound = 0

    while True:

        for i in range(upper_bound):

            print_01_codes('', n)

        if upper_bound == m:

            break
        upper_bound += 1

print_all_codes(3, 7)
