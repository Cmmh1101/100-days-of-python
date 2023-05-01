#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# foop by range based on input provided 
# random values
# output concatenating values 

password = ''

for num_let in range(1, nr_letters + 1):
    random_letters = random.choice(letters)
    password += random_letters

for num_sym in range(1, nr_symbols + 1 ):
    random_symb = random.choice(symbols)
    password += random_symb

for num_number in range(1, nr_numbers + 1):
    random_numbers = random.choice(numbers)
    password += random_numbers

print(password)

list_str = list(password)
random.shuffle(list_str)
result = ''.join(list_str)
print(f'Your password is: {result}')



