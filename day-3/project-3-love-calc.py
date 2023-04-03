print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

all_names = name1 + " " + name2
print(all_names)


T = all_names.count("t")
R = all_names.count("r")
U = all_names.count("u")
E = all_names.count("e")
true_total = str(T + R + U + E)

L = all_names.count("l")
O = all_names.count("o")
V = all_names.count("v")
E = all_names.count("e")
love_total = str(L + O + V + E)

score = int(true_total + love_total)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")