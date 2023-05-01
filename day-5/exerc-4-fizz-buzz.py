#Write your code below this row 👇

# loop

for number in range(1, 101):
    #  check div by 3 = Fizz
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    #  check if div by 5 = Buzz 
    elif number % 3 == 0:
        print('Fizz')
    # check is divisible by 3 AND 5 = FizzBuzz
    elif number % 5 == 0:
        print("Buzz")
    else:    
        print(number)