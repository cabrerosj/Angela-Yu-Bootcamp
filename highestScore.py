# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores\n").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
highestScore = 0

for i in student_scores:
    if i > highestScore:
        highestScore = i
print(f"The highest score in the class is: {highestScore}")

# You can also use the max() or min() function.
# i.e. max(student_scores)