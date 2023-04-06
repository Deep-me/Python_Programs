# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI=weight/height**2
if BMI<18.5:
    print(f"Your BMI is {round(BMI)}, you are underweight.")
elif BMI>=18.5 and BMI<25:
    print(f"Your BMI is {round(BMI)}, you have a normal weight.")
elif BMI<30:
    print(f"Your BMI is {round(BMI)}, you are slightly overweight.")
elif BMI<35:
    print(f"Your BMI is {round(BMI)}, you are obese.")
else:
    print("Your BMI is %f, you are clinically obese."%(round(BMI)))