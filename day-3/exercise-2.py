# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi_result = round(weight / (height * height))

if bmi_result < 18.5:
    print(f"Your BMI is {bmi_result}, you are underweight.")
elif bmi_result < 25:
    print(f"Your BMI is {bmi_result}, you have a normal weight.")
elif bmi_result < 30:
    print(f"Your BMI is {bmi_result}, you are slightly overweight.")
elif bmi_result < 35:
    print(f"Your BMI is {bmi_result}, you are obese.")
else:
    print(f"Your BMI is 40, you are clinically obese.")