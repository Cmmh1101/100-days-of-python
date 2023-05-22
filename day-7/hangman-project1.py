import random
#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)
print(chosen_word)

display = []

for letter in chosen_word:
    display.append('_')

print(''.join(display))

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input('Guess a letter of this word\n').lower()
# print(guess)

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

# finding = chosen_word.index(guess)
# print(finding)

for letter in chosen_word:
    if letter == guess:
        print('match')
    else:
        print("wrong")

