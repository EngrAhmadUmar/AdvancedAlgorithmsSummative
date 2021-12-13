def superDigit(n, k):
    # Initializing the variable total to store the current sum of the digit in n
    result = 0

    # Creating a variable p to store the concatenation (n times k)
    p = int(n * k)

    # Here we run a while loop while p is greater than zero and total is less than 9
    while (p > 0 or result > 9):
        # When p is not equal to 0, we use the total value, add the modulo of p to it
        # And also drop the last digit by dividing it by 10
        if (p != 0):
            result += p % 10
            p //= 10

        # Else are done adding so we swap our p and total variable
        # Then we continue searching for your super value.
        else:
            p, result = result, p

    # Returning our result.
    return result
# Test cases
n = '9875'
k = 4
print("n = " + str(n) + ', k = ' + str(k) + ', concatenated value = ' + str(n * k) + " and the super digit = " + str(
    superDigit(n, k)))

n = '148'
k = 3
print("n = " + str(n) + ', k = ' + str(k) + ', concatenated value = ' + str(n * k) + " and the super digit = " + str(
    superDigit(n, k)))

# Extra Edge Case
n = '4534'
k = 6
print("n = " + str(n) + ', k = ' + str(k) + ', concatenated value = ' + str(n * k) + " and the super digit = " + str(
    superDigit(n, k)))
