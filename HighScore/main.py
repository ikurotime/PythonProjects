students_scores = input('Input a list of students score\n').split()
# Transforms the input of students_scores, from string to int
for n in range(0, len(students_scores)):
    students_scores[n] = int(students_scores[n])

print('The highest score in the class is: ' + str(max(students_scores)))
