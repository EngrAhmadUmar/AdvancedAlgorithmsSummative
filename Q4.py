def superDigit(n, k):
    # Initializing the variable total to store the current sum of the digit in n
    total = 0

    # Creating a variable p to store the concatenation (n times k)
    p = int(n * k)

    # Here we run a while loop while p is greater than zero and total is less than 9
    while (p > 0 or total > 9):
        # When p is equal to 0, then we are done adding so we swap our p and total variable
        # Then we continue searching for your super value.
        if (p == 0):
            p, total = total, p

        # We use the total value, add the modulo of p to it
        # And also drop the last digit by dividing it by 10
        else:
            total += p % 10
            p //= 10

    # Returning our result.
    return total

# Test cases
n = '9875'
k = 4
print("n = " + str(n) + ', k = ' + str(k) + ', concatenated value = ' + str(n * k) + " and the superdigit = " + str(
    superDigit(n, k)))

n = '148'
k = 3
print("n = " + str(n) + ', k = ' + str(k) + ', concatenated value = ' + str(n * k) + " and the superdigit = " + str(
    superDigit(n, k)))
