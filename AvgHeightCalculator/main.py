student_height = input('Input a list of student heights \n').split()
print('Strings ' + str(student_height))  # This will return a list of String values.
# For each value in student_height , transform it in a int value of themselves.
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])

print('Ints ' + str(student_height))  # This will return a list of Int values.
sum_heights = sum(student_height)     # Simple maths
totalStudents = len(student_height)   # The number of students is equal to the number of values in students_height
avg_height = sum_heights/totalStudents  # Simple maths again

print('Total height = ' + str(sum_heights))
print('Students = ' + str(totalStudents))
print('Avg height = ' + str(avg_height))