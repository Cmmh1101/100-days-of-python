# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
weight_num = float(weight)
height_num = float(height)

print(round(weight_num / (height_num * height_num)))