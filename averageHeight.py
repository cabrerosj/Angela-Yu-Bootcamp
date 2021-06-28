student_heights = input("Input a list of student heights:\n").split()
totalHeights = 0
for i in student_heights:
    totalHeights += int(i)
averageHeight = round(totalHeights / len(student_heights))
print(f"The total heights for the students is {totalHeights}.\nThe average height for the students is {averageHeight}")

# **********  Below doesn't use sum() or len()  **********

# totalHeights = 0
# for student in student_heights:
#     totalHeights += student
# print(f"Total for all the heights is {totalHeights}.")

# numberOfStudents = 0
# for count in student_heights:
#     numberOfStudents += 1
# print(f"The number of students is {numberOfStudents}.")

# averageHeights = round(totalHeights / numberOfStudents)

# print(f"The average height of the {numberOfStudents} students is {averageHeights}.")