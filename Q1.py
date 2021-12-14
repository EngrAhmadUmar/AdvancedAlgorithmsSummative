# Initializing my function to return my nth sum.
def nth_sum(n):
    # Creating the result variable to help keep track of my sum
    total = 0

    # Looping through the range of the number and adding the index to the result variable
    for numbers in range(1, n + 1):
        total += numbers

    # Returning the result
    return total


# Calling the time function to help calculate the time difference for different types of inputs.
import time

start = time.process_time()
print("Input: 10, and result is: " + str(nth_sum(10)) + ' and the time taken: ' + str(time.process_time() - start) + "secs")
print("Input: 10000, and result is: " + str(nth_sum(10000)) + ' and the time taken: ' + str(
    time.process_time() - start) + "secs")
print("Input: 1000000, and result is: " + str(nth_sum(1000000)) + ' and the time taken: ' + str(
    time.process_time() - start) + "secs")
print("Input: 100000000, and result is: " + str(nth_sum(1000000000)) + ' and the time taken: ' + str(
    time.process_time() - start) + "secs")
