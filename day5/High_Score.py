# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
temp = 0
for x in range(0,len(student_scores)):
    for y in range(0,len(student_scores)):
        if student_scores[x]<student_scores[y]:
            temp = student_scores[x]
            student_scores[x]=student_scores[y]
            student_scores[y]=temp
i = student_scores[len(student_scores)-1]
print(f"The highest score in the class is: {i}")

    