# Importing the math library to help me round up my values
import math

original_grade = [73, 38, 67, 33]
# Initializing a function to take the list of the grades and return the results
def gradingStudents(grade):
    # Initializing a result.
    final_grade = []

    # Looping through the grades.
    for grade in original_grade:
        # If the grade was less than 38 we do not need to round it up because there are failing already.
        if grade < 38:
            # We directly append the grade to our result.
            final_grade.append(grade)
        else:
            # If the grade is higher than 38, find the nearest multiple
            # To the nearest whole number.
            rounded_grade = math.ceil(grade / 5) * 5

            # If the difference between new grade and grade is less than 3, the rounded grade final grade array can be appended.
            # Otherwise, the original grade is appended to the final grade array.
            if rounded_grade - grade < 3:
                final_grade.append(rounded_grade)
            else:
                final_grade.append(grade)

    # returning our rounded grades
    return final_grade


print("Original grades are: " + str(original_grade))
print("Rounded  grades are: " + str(gradingStudents(original_grade)))
