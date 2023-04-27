import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper ='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors ='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#Write your code below this line 👇

choices = [rock, paper, scissors]

user = 0
computer = 0

for i in range(5):
    playUser = int(input("Type: 1 (for rock), 2 (for paper), 3 (scissors) \n"))
    
    comp_play = random.randint(0, 2)

    print(f"you: {choices[playUser - 1]} - computer: {choices[comp_play]}")

    if playUser - 1 == 0 and comp_play == 2:
        user =+ 1
        print("You won")
    elif comp_play == 0 and playUser - 1 == 2:
        computer =+ 1
        print("You lose")
    elif playUser - 1 == 1 and comp_play == 0:
        user =+ 1
        print("You won")
    elif comp_play == 1 and playUser - 1 == 0:
        computer =+ 1
        print("You lose")
    elif playUser - 1 == 2 and comp_play == 1:
        user =+ 1
        print("You won")
    elif comp_play == 2 and playUser - 1 == 1:
        computer =+ 1
        print("You lose")
    elif playUser - 1 == comp_play:
        print("it's a tie")
    else:
        print("You typed an invalid number, you lose!")

    print(f"computer: {computer} - You: {user}")


    print("Game over")
    if computer > user:
        print("You lose!")
    elif computer < user:
        print("You won!!!!")
    else:
        print("It's a tie")

    print(f"computer: {computer} - You: {user}")




